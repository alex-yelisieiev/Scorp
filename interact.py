from rich import console
from rich.console import Console
from requests import get


console = Console(style='cyan')


def sayHi():
    console.print(
        '''
        Hey! Welcome to [white]Scorp[/white] - a tool for scrappig news,
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
        link = str(input())
        try:
            if get(link) == '200':
                console.print('Enter word(s) divided by \', \': ')
                words = str(input()).split(', ')
                scrapObject.addScrap(*words, url=link)
            else:
                console.print('There\'s a problem with this page', style='red')
        except:
            console.print('There\'s a problem with this page', style='red')

    elif inp == 'delete':
        console.print('Enter link: ', end='')
        link = str(input())
        console.print('Enter word(s) divided to be deleted by \', \': ')
        words = str(input()).split(', ')
        scrapObject.delScrap(*words, url=link)
    
    elif inp == 'refresh found':
        scrapObject.clrFoundUrls()

    elif inp == 'refresh units':
        scrapObject.clrScraps()

    elif inp == 'scan':
        scrapObject.runScan()

    elif inp == 'esc' or inp == 'escape' or inp == 'exit':
        quit()
