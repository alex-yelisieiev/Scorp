from rich.console import Console


console = Console()

banner = r'''  ____
/\  _`\
\ \,\L\_\    ___  _ __   __    _____   _____   __  __
 \/_\__ \   /'___/\`'__/'__`\ /\ '__`\/\ '__`\/\ \/\ \
   /\ \L\ \/\ \__\ \ \/\ \L\.\\ \ \L\ \ \ \L\ \ \ \_\ \
   \ `\____\ \____\ \_\ \__/.\_\ \ ,__/\ \ ,__/\/`____ \
    \/_____/\/____/\/_/\/__/\/_/\ \ \/  \ \ \/  `/___/> \
                                 \ \_\   \ \_\     /\___/
                                  \/_/    \/_/     \/__/'''

subBanner = '''Made by Alex Yelisieiev
My facebook: [blue]https://www.facebook.com/profile.php?id=100015304577934[/blue]
For help print [blue]\'help\'[blue]\n'''

console.print(banner, style='cyan', highlight=False)
console.print(subBanner, style='cyan', highlight=False)