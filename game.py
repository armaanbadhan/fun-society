from random import randint

UP = '\033[1A'
CLEAR = '\x1b[2K'

MAX_WIDTH = 32
MAX_HEIGHT = 16
CELLS = [(col, row) for row in range(MAX_HEIGHT) for col in range(MAX_WIDTH)]


def update_apple():
    return (randint(1, MAX_WIDTH - 1), randint(1, MAX_HEIGHT - 1))
    

def print_field(apple_pos):
    for cell in CELLS:
        if cell[0] in (0, MAX_WIDTH - 1) or cell[1] in (0, MAX_HEIGHT - 1):
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
    print(UP*MAX_HEIGHT, end=CLEAR)
