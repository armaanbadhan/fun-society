import os
import msvcrt  # check os then import msvcrt/getch
from util.cursor import Cursor

from games.snake import play_snake

os.system('mode con: cols=100 lines=27')

cur = Cursor()

BANNER = [
    "███████╗██╗   ██╗███╗   ██╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗",
    "██╔════╝██║   ██║████╗  ██║     ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝",
    "█████╗  ██║   ██║██╔██╗ ██║     ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ ",
    "██╔══╝  ██║   ██║██║╚██╗██║     ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  ",
    "██║     ╚██████╔╝██║ ╚████║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ",
    "╚═╝      ╚═════╝ ╚═╝  ╚═══╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ",
]
INFO = """
Ned Bosham reopened the arcade under the name "Fun Society Amusement, LLC". In August 2013, Harold 
Bosham pressed his father to sell the property; when that failed, Harold stole his twin brother's 
hunting rifle and shot Ned in the face. The rifle kicked back so hard, he tripped and fell out of 
a 20-story window. Harold's twin brother Clyde was arrested for double homicide and sent to prison, 
where he became Romero's cellmate. When Romero was released, he received the keys from Clyde, who 
urged him to burn it down; instead, Romero took advantage of the building's legal limbo to 
create an anonymous safehouse.
"""


# TODO: store game_name, game function, arrow params somethere
ARROW_POSITION = {   # (call param) : (down, right)
    (0, 0): (22, 16),
    (0, 1): (22, 42),
    (1, 0): (23, 16),
    (1, 1): (23, 42),
    (2, 0): (24, 16),
    (2, 1): (24, 42),
    (3, 0): (26, 42),
    (3, 1): (26, 42),
}



class Arrow:
    def __init__(self) -> None:
        self.arrow  = "-->\r"
        self.eraser = "   \r"
        self.position = None

    
    def display(self, pos):
        self.erase()
        self.position = pos
        posi = ARROW_POSITION[pos]
        cur.tprint(self.arrow, pos_x=posi[1], pos_y=posi[0])

    
    def erase(self):
        if self.position is not None:
            posi = ARROW_POSITION[self.position]
            cur.tprint(self.eraser, pos_x=posi[1], pos_y=posi[0])


# TODO: show score on this and "press this to comtinue"
def play_games(x, y):
    if (x, y) == (0, 0):
        score = play_snake()
        return
    else:
        cur.tprint("game will be implimented soon")
        exit()


# TODO: border around the whole thing?
def show_menu():
    cur.clear_all()
    cur.tprint("\n\n", pos_x=0, pos_y=0)

    for ban in BANNER:
        cur.tprint("        " + ban + '\n', color=cur.RED)

    cur.tprint('\n' + INFO + '\n\n', color=cur.LIGHT_RED)

    cur.tprint(" "*30)
    cur.tprint("***Welcome to Fun-Society***\n\n", negative=True, blink=True, color=cur.GREEN)

    cur.tprint("choose the game you wanna play(w/a/s/d/enter):\n", color=cur.BLUE)

    cur.tprint(" "*20 + "snake " + " "*20 + "pong  " + '\n', color=cur.LIGHT_CYAN)
    cur.tprint(" "*20 + "game 3" + " "*20 + "game 4" + '\n', color=cur.LIGHT_CYAN)
    cur.tprint(" "*20 + "game 5" + " "*20 + "game 6" + '\n\n', color=cur.LIGHT_CYAN)

    cur.tprint(" "*20 + "      " + " "*20)
    cur.tprint("exit", underline=True, color=cur.LIGHT_CYAN)

    arrow = Arrow()
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
            os.system('cls')
            if point_to_x == 3:
                cur.tprint('THANKS FOR PLAYING')
                exit()
            play_games(point_to_x, point_to_y)
            break


while True:
    show_menu()
