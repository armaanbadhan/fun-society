from os import get_terminal_size
import os
import msvcrt

# TODO: hide cursor
# ref: https://superuser.com/questions/1496322/how-do-i-remove-hide-the-cursor-the-blinking-underscore-character-in-cmd-exe

# ANSI Characters
RESET = "\033c"
HOME = "\033[;H"

UP =      '\033[1A'
DOWN =    '\033[1B'
FORWARD = '\033[1C'
BACK =    '\033[1D'

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

BANNER = [
    "███████╗██╗   ██╗███╗   ██╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗",
    "██╔════╝██║   ██║████╗  ██║     ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝",
    "█████╗  ██║   ██║██╔██╗ ██║     ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ ",
    "██╔══╝  ██║   ██║██║╚██╗██║     ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  ",
    "██║     ╚██████╔╝██║ ╚████║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ",
    "╚═╝      ╚═════╝ ╚═╝  ╚═══╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ",
]
INFO = """
Ned Bosham reopened the arcade under the name "Fun Society Amusement, LLC". In August 2013, Harold Bosham 
pressed his father to sell the property; when that failed, Harold stole his twin brother's hunting rifle
and shot Ned in the face. The rifle kicked back so hard, he tripped and fell out of a 20-story window. 
Harold's twin brother Clyde was arrested for double homicide and sent to prison, where he became Romero's 
cellmate. When Romero was released, he received the keys from Clyde, who urged him to burn it down; instead, 
Romero took advantage of the building's legal limbo to create an anonymous safehouse.
"""


ARROW_POSITION = {   # (call param) : (down, right)
    (0, 0): (20, 12),
    (0, 1): (20, 38),
    (1, 0): (21, 12),
    (1, 1): (21, 38),
    (2, 0): (22, 12),
    (2, 1): (22, 38),
    (3, 0): (24, 38),
    (3, 1): (24, 38),
}


class Arrow:
    def __init__(self) -> None:
        self.arrow  = "    -->"
        self.eraser = "       "
        self.position = (0, 0)
        self.display(self.position)

    def set_initial(self):
        return
    
    def display(self, pos):
        self.erase()
        self.position = pos
        posi = ARROW_POSITION[pos]
        print(HOME + DOWN*posi[0] + FORWARD*posi[1] + RESET_COLOR + self.arrow, end='\r')

    
    def erase(self):
        posi = ARROW_POSITION[self.position]
        print(HOME + DOWN*posi[0] + FORWARD*posi[1] + RESET_COLOR + self.eraser, end='\r')
        return




print(RESET)

for ban in BANNER:
    print(RED + "        " + ban)

print(INFO)

print("***Welcome to Fun-Society***\n\n")       # TODO: make it blink somehow

print(LIGHT_CYAN + GO_TO_START_OF_LINE + "choose the game you wanna play(w/a/s/d/enter):\n" + LIGHT_BLUE)

print(" "*20 + "game 1" + " "*20 + "game 2")
print(" "*20 + "game 3" + " "*20 + "game 4")
print(" "*20 + "game 5" + " "*20 + "game 6")
print("")
print(" "*20 + "      " + " "*20 + UNDERLINE + "exit")

arrow = Arrow()


# TODO: border around the whole thing?


point_to_x, point_to_y = 0, 0

while True:
    arrow.display((point_to_x, point_to_y))
    char = msvcrt.getch().decode("utf-8")

    if char in ('a', 'd'):
        point_to_y = (point_to_y + 1) % 2
    elif char == 'w':
        point_to_x = (point_to_x + 3) % 4
    elif char == 's':
        point_to_x = (point_to_x + 1) % 4
    elif char == '\r':
        print("you chose", point_to_x, point_to_y)
        break


print(RESET_COLOR)
