from scrapping import Scraper
from rich.console import Console
import __init__


# TODO: Add check for help
# TODO: Add a user interaction module

scrap = Scraper()
scrap.clrScraps()
scrap.clrFoundUrls()
scrap.addScrap('telegram', 'data', url='https://moodle3.chmnu.edu.ua/')
scrap.runScan()

input()