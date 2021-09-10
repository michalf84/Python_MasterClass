numbers=(0,1,2,3,4,5)

print(numbers, sep=';')
print(*numbers, sep=';')

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,4,5,6)

print("emty interesting")
print("empty one:", test_star())
print()
print()



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


print(RED,"random teks")
print("other")
print(RESET)
print("czarny")
def drukowanie(text: str, *effects: str) -> None:
    """
    Print text using ansi squeneces to change colour
    :param tekst: the text to print
    :param effects: the effects we want
    :param effect: effeect we wnt
    :return:
    """
    effect_string="".join(effects)
    output_string=f"{effect_string}{text}{RESET}"
    print(output_string)

drukowanie("Hello Michale",WHITE)
drukowanie("Hello Michale",MAGENTA)
drukowanie("Hello eorls",BLUE,REVERSE,UNDERLINE)