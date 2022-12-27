from os import get_terminal_size
import os

# https://stackoverflow.com/questions/37774983/clearing-the-screen-by-printing-a-character


# ANSI Characters
RESET = "\033c"
UP = '\033[1A'
DOWN = '\033[1B'
CLEAR = '\033[2K'
RESET_COLOR = '\033[0m'
GO_TO_START_OF_LINE = "\r"
# make sure to use \r after if using at start of a line
RED = '\033[0;31m'
LIGHT_BLUE = '\033[1;34m'


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


print(RESET)

for ban in banner:
    print(RED + "        " + ban)

print(DOWN*5)

print()