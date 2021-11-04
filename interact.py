import requests
from rich import console
from rich.console import Console
from requests import get


console = Console(style='cyan')


def sayHi():
    console.print(
        '''
        Hey! Welcome to [white]Scorp[/white] - a tool for scrappig news pages,
        profiles or any pages containing links.

        If you want to search for some word(s), firstly
        you'll have to create a [white]search unit[/white]. It's so
        simple: just print [white]add[/white] and follow instructions.
        For example:
        add
        Enter link: https://www.nytimes.com/
        Enter word(s): coronavirus, data leak
        Done! This will create a search unit with
        keys 'coronavirus' and 'data leak'
        To run scan print [white]scan[/white]
        Print [white]delete[/white] to remove word(s) from a search unit.
        
        [white]Warning![/white] The program remembers all your search units
        and already found words, so there's no need to
        create search units everytime you run it. It won't
        show you a word if it was already found.
        
        To refresh found words list print [white]refresh found[/white]
        To refresh delete all search units print [white]refresh units[/white]
        Print [white]esc[/white], [white]exit[/white] or [white]escape[/white] to exit.
        ''',
        highlight=False
    )

def anlz(scrapObject, inp: str):
    inp = str(inp).strip().lower()
    
    if '-h' in inp or 'help' in inp:
        sayHi()

    elif inp == 'add':
        console.print('Enter link: ', end='')
        link = str(input()).strip()
        if link:
            try:
                response = get(link)
                if response.status_code == 200:
                    console.print('Enter word(s) divided by \', \': ', highlight=False)
                    words = str(input()).split(', ')
                    scrapObject.addScrap(*words, url=link)
                else:
                    console.print('[red]There\'s a problem with this page. Try another one[/red]')
            except:
                console.print('[red]There\'s a problem with this page. Try another one[/red]')
        else:
            console.print('Cancelled')

    elif inp == 'delete':
        console.print('Enter link: ', end='')
        link = str(input())
        if link:
            console.print('Enter word(s) divided to be deleted by \', \': ', highlight=False)
            words = str(input()).split(', ')
            scrapObject.delScrap(*words, url=link)
        else:
            console.print('Cancelled')
    
    elif inp == 'clear found links':
        scrapObject.clrFoundUrls()
        console.print('Found links list cleared')

    elif inp == 'clear scraps':
        scrapObject.clrScraps()
        console.print('Scraps list cleared')

    elif inp == 'scan':
        scrapObject.runScan()

    elif inp == 'show scraps':
        scrapObject.showScraps()
        
    elif inp == 'show found links':
        scrapObject.showFoundUrls()

    elif inp == 'esc' or inp == 'escape' or inp == 'exit':
        quit()
