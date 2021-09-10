# Some ANSI escape sequences for colours and effects
import colorama
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


#colorama allows us in terminal to see some effects,
# no need to use

colorama.init()
print(RED,"random teks")
print("other")
print(RESET)
print("czarny")
def drukowanie(text: str, effect: str) -> None:
    """
    Print text using ansi squeneces to change colour
    :param tekst: the text to print
    :param effect: effeect we wnt
    :return:
    """
    output_string=f"{effect}{text}{RESET}"
    print(output_string)

drukowanie("Hello Michale",WHITE)
drukowanie("Hello Michale",MAGENTA)
colorama.deinit()