import bs4
import requests
import json
from urllib.parse import urljoin
from rich.console import Console


console = Console(style='cyan')


class Scraper(object):

    def clrScraps(self):
        with open('./Scraps.json', 'w'):
            console.print('Search list\'s been cleared')

    def clrFoundUrls(self):
        with open('./FoundUrls.json', 'w'):
            console.print('Found links list\'s been cleared')

    def delScrap(self, *args, url):
        data = self.getScraps()
        if data:
            for keyword in args:
                try:
                    data[url].remove(keyword)
                except:
                    console.print(
                        f'[red]Word [white]\'{keyword}\'[/white] isn\'t in search unit[/red]', highlight=False)
                with open('./Scraps.json', 'w') as fileWrite:
                    json.dump(data, fileWrite)
        else:
            console.print(f'[red]No data found[/red]')

    def getFoundUrls(self):
        try:
            with open('./FoundUrls.json', 'r') as fileRead:
                data = json.load(fileRead)
                return data
        except:
            return None

    def wordSearch(self, *args, url):
        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, features='lxml')
        aTags = soup.find_all('a')
        tagsWithKey = {}

        # Search for a word in the list of a elements
        for keyword in args:
            for tag in aTags:
                if keyword.lower() in str(tag.contents).lower():

                    # Get full href
                    fullUrl = urljoin(url, tag.get('href'))

                    # Add to the final answers and found urls

                    # Add a url to already found ones or make a
                    # new file with found urls if there's no such a file
                    try:
                        with open('./FoundUrls.json', 'r') as fileRead:
                            data = json.load(fileRead)
                            if fullUrl.split('/')[-1] not in data:
                                try:
                                    tagsWithKey[keyword].extend([fullUrl])
                                except:
                                    tagsWithKey[keyword] = [fullUrl]
                                data.append(fullUrl.split('/')[-1])

                            with open('./FoundUrls.json', 'w') as fileWrite:
                                json.dump(data, fileWrite)

                    except:
                        with open('./FoundUrls.json', 'w') as fileWrite:
                            tagsWithKey[keyword] = []
                            tagsWithKey[keyword].append(fullUrl)
                            data = []
                            data.append(fullUrl.split('/')[-1])
                            json.dump(data, fileWrite)
        return tagsWithKey

    def getScraps(self):
        try:
            with open('./Scraps.json', 'r') as jsonFile:
                scraps = json.load(jsonFile)
                return scraps
        except:
            return None

    def addScrap(self, *args, url):
        # Make data if there is previous info
        if self.getScraps():
            data = self.getScraps()

            # Append search in some url
            if url in data.keys():
                for keyword in args:
                    if keyword not in data[url]:
                        data[url].append(keyword)
                        console.print(
                            f'Search at [white]{url}[/white] expanded')
                    else:
                        console.print(
                            f'[red]Word [white]\'{keyword}\'[/white] is already in search unit[/red]')

        # Make data if there is no previous info
        else:
            data = {}
            data[url] = args
            console.print(f'Search at [white]{url}[/white] expanded')
        with open('./Scraps.json', 'w') as fileWrite:
            json.dump(data, fileWrite)

    def runScan(self):
        data = self.getScraps()
        if data:
            # Search for all keywords
            for key in data.keys():  # Keys are urls in Scraps.json
                foundHrefs = self.wordSearch(*data[key], url=key)
                if foundHrefs:
                    for keyword in foundHrefs.keys():
                        urlList = foundHrefs[keyword]
                        for url in urlList:
                            console.print(
                                f'Found url [white]{url}[/white] for keyword [white]\'{keyword}\'[/white]', highlight=False)

    def delFoundInfo(self):
        try:
            with open('./FoundUrls.json', 'w'):
                console.print('Info\'s been deleted succesfully')
        except:
            console.print('[red]No info to be deleted[/red]')
