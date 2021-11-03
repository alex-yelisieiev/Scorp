from rich import console
from rich.console import Console


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
        Done! This will create a search unit with keys 'coronavirus' and 'data leak'
        To run scan print [white]scan[/white]
        Print [white]delete[/white] to remove a word(s) from a search unit.
        
        [white]Warning![/white] The program remembers all your search units
        and already found words, so there's no need to
        create search units everytime you run it. It won't
        show you a word if it was already found.
        
        To refresh found words list print [white]refresh found[/white]
        To refresh delete all search units print [white]refresh units[/white]
        ''',
        highlight=False
    )


def anlz(scrapObject, inp: str):
    inp = str(inp).strip().lower()
    
    if '-h' in inp or 'help' in inp:
        sayHi()
