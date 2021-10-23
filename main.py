from re import S
from scrapping import Scraper
import __init__


# TODO: Add check for help
# TODO: Add functions to clear Scraps.json and FoundUrls.json
# TODO: Add voice commands (maybe)

# BUG: runScan shows even already found urls

scrap = Scraper()
scrap.addScrap('telegram', 'data', url='https://moodle3.chmnu.edu.ua/')
scrap.delScrap('data', 'b', url='https://moodle3.chmnu.edu.ua/')
scrap.runScan()

input()