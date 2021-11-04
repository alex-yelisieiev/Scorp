from rich.console import Console


console = Console(style='cyan')

banner = r'''
  ██████  ▄████▄   ▒█████   ██▀███   ██▓███  
▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▓██[blue]░[/blue]  ██▒
[blue]░[/blue] ▓██▄   ▒▓█    ▄ ▒██[blue]░[/blue]  ██▒▓██ [blue]░[/blue]▄█ ▒▓██[blue]░[/blue] ██▓▒
  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██[blue]░[/blue]▒██▀▀█▄  ▒██▄█▓▒ ▒
▒██████▒▒▒ ▓███▀ [blue]░[/blue][blue]░[/blue] ████▓▒[blue]░[/blue][blue]░[/blue]██▓ ▒██▒▒██▒ [blue]░[/blue]  [blue]░[/blue]
▒ ▒▓▒ ▒ [blue]░[/blue][blue]░[/blue] [blue]░[/blue]▒ ▒  [blue]░[/blue][blue]░[/blue] ▒[blue]░[/blue]▒[blue]░[/blue]▒[blue]░[/blue] [blue]░[/blue] ▒▓ [blue]░[/blue]▒▓[blue]░[/blue]▒▓▒[blue]░[/blue] [blue]░[/blue]  [blue]░[/blue]
[blue]░[/blue] [blue]░[/blue]▒  [blue]░[/blue] [blue]░[/blue]  [blue]░[/blue]  ▒     [blue]░[/blue] ▒ ▒[blue]░[/blue]   [blue]░[/blue]▒ [blue]░[/blue] ▒[blue]░[/blue][blue]░[/blue]▒ [blue]░[/blue]     
[blue]░[/blue]  [blue]░[/blue]  [blue]░[/blue]  [blue]░[/blue]        [blue]░[/blue] [blue]░[/blue] [blue]░[/blue] ▒    [blue]░[/blue][blue]░[/blue]   [blue]░[/blue] [blue]░[/blue][blue]░[/blue]       
      [blue]░[/blue]  [blue]░[/blue] [blue]░[/blue]          [blue]░[/blue] [blue]░[/blue]     [blue]░[/blue]              
         [blue]░[/blue]                                   
'''

subBanner = '''Made by Alex Yelisieiev
My facebook: [white]https://www.facebook.com/profile.php?id=100015304577934[/white]
For help print [white]\'help\'[white]\n'''

console.print(banner, highlight=False)
console.print(subBanner, highlight=False)