from scrapping import Scraper
from rich.console import Console
import interact as inter
import __init__


# TODO: Add facebook scrapping (maybe also add friends
# chains) with facebook scrapping module

scrap = Scraper()

while True:
    inter.anlz(scrap, input())