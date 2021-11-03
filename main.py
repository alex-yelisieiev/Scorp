from scrapping import Scraper
from rich.console import Console
import interact as inter
import __init__


# TODO: Add a user interaction module
# TODO: Add facebook scrapping (maybe also add friends
# chains) with facebook scrapping module
# TODO: improve anlz func

scrap = Scraper()

inter.anlz(scrap, input())

input()