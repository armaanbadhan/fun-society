from os import get_terminal_size
import os

# TODO: hide cursor
# ref: https://superuser.com/questions/1496322/how-do-i-remove-hide-the-cursor-the-blinking-underscore-character-in-cmd-exe

# ANSI Characters
RESET = "\033c"
UP = '\033[1A'
DOWN = '\033[1B'
CLEAR = '\033[2K'
GO_TO_START_OF_LINE = "\r"
# make sure to use \r after if using at start of a line

UNDERLINE = "\033[4m"
RED = '\033[0;31m'
LIGHT_CYAN = "\033[1;36m"
LIGHT_BLUE = '\033[1;34m'
RESET_COLOR = '\033[0m'


os.system('mode con: cols=100 lines=40')


term_size = get_terminal_size()

MAX_WIDTH = term_size.columns
MAX_HEIGHT = term_size.lines

banner = [
    "███████╗██╗   ██╗███╗   ██╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗",
    "██╔════╝██║   ██║████╗  ██║     ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝",
    "█████╗  ██║   ██║██╔██╗ ██║     ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ ",
    "██╔══╝  ██║   ██║██║╚██╗██║     ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  ",
    "██║     ╚██████╔╝██║ ╚████║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ",
    "╚═╝      ╚═════╝ ╚═╝  ╚═══╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ",
]
bs = """
Ned Bosham reopened the arcade under the name "Fun Society Amusement, LLC". In August 2013, Harold Bosham 
pressed his father to sell the property; when that failed, Harold stole his twin brother's hunting rifle
and shot Ned in the face. The rifle kicked back so hard, he tripped and fell out of a 20-story window. 
Harold's twin brother Clyde was arrested for double homicide and sent to prison, where he became Romero's 
cellmate. When Romero was released, he received the keys from Clyde, who urged him to burn it down; instead, 
Romero took advantage of the building's legal limbo to create an anonymous safehouse.
"""

print(RESET)

for ban in banner:
    print(RED + "        " + ban)

print(bs)

print("***Welcome to Fun-Society***")       # TODO: make it blink somehow

print(DOWN)

print(LIGHT_CYAN + GO_TO_START_OF_LINE + "choose the game you wanna play:" + DOWN + LIGHT_BLUE)

print(" "*20 + "game 1" + " "*20 + "game 2")
print(" "*20 + "game 3" + " "*20 + "game 4")
print(" "*20 + "game 5" + " "*20 + "game 6")
print("")
print(" "*20 + "      " + " "*20 + UNDERLINE + "exit")
print(RESET_COLOR)

# TODO: make a moving arrow which doesnt refresh everything
# TODO: border around the whole thing?