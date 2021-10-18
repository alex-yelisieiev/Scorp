import bs4
import requests
import json
from urllib.parse import urljoin


class Scraper(object):

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

                    # Add to the final answers

                    # Add a url to already found ones and check
                    # wheteher it's already there. If so, ignore it
                    # TODO: Finish this block
                    try: # There might be need to replace all that by getFoundUrls function
                        with open('./FoundUrls.json', 'r') as fileRead:
                            data = json.load(fileRead)
                            if fullUrl not in data:
                                tagsWithKey[keyword] = fullUrl
                                data.append(fullUrl)
                                with open('./FoundUrls.json', 'r') as fileWrite:
                                    json.dump(data, fileWrite)

                    except:
                        with open('./FoundUrls.json', 'w') as fileWrite:
                            tagsWithKey[keyword] = fullUrl
                            data = []
                            data.append(fullUrl)
                            json.dump(data, fileWrite)

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
                        print(f'Search at {url} expanded')
                    else:
                        print(f'Word {keyword} is already in search unit')

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
        data = self.getScraps()
        if not data:
            return
        
        # Search for all keywords
        for key in data.keys(): # Keys are urls in Scraps.json
            foundHrefs = self.wordSearch(*data[key], url=key)
            if foundHrefs:
                for keyword in foundHrefs.keys():
                    print(f'Found url {foundHrefs[keyword]} for keyword \'{keyword}\'')