from scrapping import Scraper
from rich.console import Console
import interact as inter
import __init__


console = Console(style='cyan')
scrap = Scraper()

while True:
    inter.anlz(scrap, console.input('>>> '))