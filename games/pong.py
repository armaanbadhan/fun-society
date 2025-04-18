from random import randint
from pytimedinput import timedInput
from colorama import Fore
import os

UP = '\033[1A'
CLEAR = '\x1b[2K'

MAX_WIDTH = 100 - 1
MAX_HEIGHT = 28

CELLS = [(col, row) for row in range(MAX_HEIGHT - 1) for col in range(MAX_WIDTH)]

DIRECTIONS = {
    'up': (0, -1),
    'down': (0, 1),
}

BALL_DIR = {
    'left': (-1, 1),
    'right': (1, -1),
    'up': (-1, -1),
    'down': (1, 1),
}


class Pong:
    def __init__(self):
        self.ball_pos = [(49, 13), (50, 13)]
        self.ball_speed = 1
        self.player_pos = MAX_WIDTH - 1
        self.comp_pos = 1
        self.paddle_speed = 1
        self.score = 0
        self.print_board()

    def print_board(self):
        for cell in CELLS:
            if cell[0] in (0, MAX_WIDTH - 1) or cell[1] in (0, MAX_HEIGHT - 2):
                print("#", end='')
                if cell[0] == MAX_WIDTH - 1:
                    print('')
            else:
                if cell in self.ball_pos:
                    print(u'\u2588', end='')
                else:
                    print(" ", end='')

    def update_ball(self):
        # erase previous ball
        # draw new ball
        dir = BALL_DIR['left']
        self.ball_pos[0][0] += dir[0]
        self.ball_pos[0][1] += dir[1]
        self.ball_pos[1][0] += dir[0]
        self.ball_pos[1][1] += dir[1]

    def play(self):
        while True:
            return self.score


def play_pong():
    pong = Pong()
    return pong.play()


if __name__ == "__main__":
#    os.system(f'mode con: cols={MAX_WIDTH} lines={MAX_HEIGHT}')
    score = play_pong()
    print(f"you scored {score}!")
