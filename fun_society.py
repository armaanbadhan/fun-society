"""
game
"""
import os
import getch 
import sys

from util.cursor import AnsiCodes
from util.cursor import print, clear_all

from games.snake import play_snake

os.system('mode con: cols=100 lines=28')


BANNER = [
    "███████╗██╗   ██╗███╗   ██╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗",
    "██╔════╝██║   ██║████╗  ██║     ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝",
    "█████╗  ██║   ██║██╔██╗ ██║     ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ ",
    "██╔══╝  ██║   ██║██║╚██╗██║     ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  ",
    "██║     ╚██████╔╝██║ ╚████║     ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   ",
    "╚═╝      ╚═════╝ ╚═╝  ╚═══╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝   ",
]
# TODO: change info xd
INFO = """
Ned Bosham reopened the arcade under the name "Fun Society Amusement, LLC". In August 2013, Harold
 Bosham pressed his father to sell the property; when that failed, Harold stole his twin brother's
 hunting rifle and shot Ned in the face. The rifle kicked back so hard, he tripped and fell out of
 a 20-story window. Harold's twin brother Clyde was arrested for double homicide and sent to prison,
 where he became Romero's cellmate. When Romero was released, he received the keys from Clyde, who
 urged him to burn it down; instead, Romero took advantage of the building's legal limbo to
 create an anonymous safe-house.
"""

# TODO: store game_name, game function, arrow params somewhere
ARROW_POSITION = {  # (call param) : (down, right)
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
        self.arrow = "-->\r"
        self.eraser = "   \r"
        self.position = None

    def display(self, pos):
        self.erase()
        self.position = pos
        position = ARROW_POSITION[pos]
        print(self.arrow, pos_x=position[1], pos_y=position[0])

    def erase(self):
        if self.position is not None:
            position = ARROW_POSITION[self.position]
            print(self.eraser, pos_x=position[1], pos_y=position[0])


# TODO: show score on this and "press this to continue"
def play_games(x, y):
    if (x, y) == (0, 0):
        score = play_snake()
        clear_all()
        print(f"YOU SCORED {score}! \npress enter to continue")
        input()
    else:
        print("game will be implemented soon")
        sys.exit()


# TODO: border around the whole thing?
def show_menu():
    """
    Shows the menu hah
    :return:
    """
    clear_all()
    print("\n\n", pos_x=0, pos_y=0)

    for ban in BANNER:
        print("        " + ban + '\n', color=AnsiCodes.RED)

    print('\n' + INFO + '\n\n', color=AnsiCodes.LIGHT_RED)

    print(" " * 30)
    print("***Welcome to Fun-Society***\n\n", negative=True, blink=True, color=AnsiCodes.GREEN)

    print("choose the game you wanna play(w/a/s/d/enter):\n", color=AnsiCodes.BLUE)

    print(" " * 20 + "snake " + " " * 20 + "pong  " + '\n', color=AnsiCodes.LIGHT_CYAN)
    print(" " * 20 + "game 3" + " " * 20 + "game 4" + '\n', color=AnsiCodes.LIGHT_CYAN)
    print(" " * 20 + "game 5" + " " * 20 + "game 6" + '\n\n', color=AnsiCodes.LIGHT_CYAN)

    print(" " * 20 + "      " + " " * 20)
    print("exit", underline=True, color=AnsiCodes.LIGHT_CYAN)

    arrow = Arrow()
    point_to_x, point_to_y = 0, 0

    while True:
        arrow.display((point_to_x, point_to_y))
        char = getch.getch()

        if char in ('a', 'd'):
            point_to_y = (point_to_y + 1) % 2
        elif char == 'w':
            point_to_x = (point_to_x + 3) % 4
        elif char == 's':
            point_to_x = (point_to_x + 1) % 4
        elif char == '\n':
            os.system('clear')
            if point_to_x == 3:
                print('THANKS FOR PLAYING')
                sys.exit()
            play_games(point_to_x, point_to_y)
            break


while True:
    show_menu()
