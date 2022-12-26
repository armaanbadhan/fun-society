from random import randint
from pytimedinput import timedInput
from os import get_terminal_size


term_size = get_terminal_size()

UP = '\033[1A'
CLEAR = '\x1b[2K'

MAX_WIDTH = term_size.columns
MAX_HEIGHT = term_size.lines - 1
CELLS = [(col, row) for row in range(MAX_HEIGHT) for col in range(MAX_WIDTH)]

DIRECTIONS = {
    'left': (-1,  0),
    'right': (1,  0),
    'up':    (0, -1),
    'down':  (0,  1),
}

snake = [
    (5, MAX_HEIGHT//2), 
    (4, MAX_HEIGHT//2), 
    (3, MAX_HEIGHT//2)
]
direction = DIRECTIONS['right']


def update_snake():
    new_head = direction[0] + snake[0][0], direction[1] + snake[0][1]
    snake.insert(0, new_head)
    snake.pop(-1)


def update_apple():
    pos = (randint(1, MAX_WIDTH - 1), randint(1, MAX_HEIGHT - 1))
    while pos in snake:
        pos = (randint(1, MAX_WIDTH - 1), randint(1, MAX_HEIGHT - 1))
    return pos
    

def print_field(apple_pos):
    for cell in CELLS:
        if cell in snake:
            print('S', end='')
        elif cell[0] in (0, MAX_WIDTH - 1) or cell[1] in (0, MAX_HEIGHT - 1):
            print("#", end='')
            if cell[0] == MAX_WIDTH - 1:
                print('')
        else:
            if cell == apple_pos:
                print('a', end='')
            else:
                print(" ", end='')


while True:
    apple_pos = update_apple()
    print_field(apple_pos)
    update_snake()
    inp, entered = timedInput('get_input:', timeout=1)
    if entered:
        match inp:
            case 'w': 
                direction = DIRECTIONS['up']
            case 'a': 
                direction = DIRECTIONS['left']
            case 's': 
                direction = DIRECTIONS['down']
            case 'd': 
                direction = DIRECTIONS['right']
    print(UP*(MAX_HEIGHT + 1), end=CLEAR)
