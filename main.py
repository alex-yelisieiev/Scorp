from scrapping import Scraper
import __init__


# TODO: Add check for help
# TODO: Add functions to clear Scraps.json and FoundUrls.json
# TODO: Add voice commands (maybe)

# TODO: Add rich module colorizing (already installed)

scrap = Scraper()
scrap.addNewScrap('data', 'telegram', url='https://moodle3.chmnu.edu.ua/')
scrap.delScrap('https://moodle3.chmnu.edu.ua/', 'telegram', 'data')
scrap.runScan()

input()