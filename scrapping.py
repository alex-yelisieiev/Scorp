import bs4
import requests
import json
from urllib.parse import urljoin


class Scraper(object):

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

                    # Add to the final answers
                    tagsWithKey[keyword] = fullUrl

        return tagsWithKey

    def getScraps(self):
        try:
            with open('./Scraps.json', 'r') as jsonFile:
                scraps = json.load(jsonFile)
                return scraps
        except:
            return None

    def addNewScrap(self, *args, url):
        # Make data if there is previous info
        if self.getScraps():
            data = self.getScraps()

            # Append search in some url
            if url in data.keys():
                for keyword in args:
                    if keyword not in data[url]:
                        data[url].append(keyword)
                    else:
                        print(f'Word {keyword} is already in search unit')
                print(f'Search at {url} expanded')

        # Make data if there is no previous info
        else:
            data = {}
            data[url] = args
            print(f'Search at {url} added')
        with open('./Scraps.json', 'w') as fileWrite:
            json.dump(data, fileWrite)

    def delScrap(self, url):
        try:
            data = self.getScraps()
            data.pop(url)
            with open('./Scraps.json', 'w') as file:
                json.dump(data, file)
        except:
            print('Such url doesn\'t exist')

    def runScan(self):
        data = self.getScraps() # TODO: Вот тут дописать лоад текущих тасков поиска и сам поиск
        if not data:
            return
        
        # Search for all keywords
        for key in data.keys(): # Keys are urls in Scraps.json
            foundHrefs = self.wordSearch(*data[key], url=key)
            if foundHrefs:
                for keyword in foundHrefs.keys():
                    print(f'Found url {foundHrefs[keyword]} for keyword \'{keyword}\'')