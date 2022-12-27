from random import randint
from pytimedinput import timedInput
from os import get_terminal_size


UP = '\033[1A'
CLEAR = '\x1b[2K'

term_size = get_terminal_size()
MAX_WIDTH = term_size.columns
MAX_HEIGHT = term_size.lines - 1

CELLS = [(col, row) for row in range(MAX_HEIGHT) for col in range(MAX_WIDTH)]

DIRECTIONS = {
    'left': (-1,  0),
    'right': (1,  0),
    'up':    (0, -1),
    'down':  (0,  1),
}


class SnakeGame:
    def __init__(self):
        self.snake = [(5, MAX_HEIGHT//2), (4, MAX_HEIGHT//2), (3, MAX_HEIGHT//2)]
        self.direction = DIRECTIONS['right']
        self.apple_pos = None
        self.eaten = False
        self.update_apple()


    def update_snake(self):
        new_head = self.direction[0] + self.snake[0][0], self.direction[1] + self.snake[0][1]
        self.snake.insert(0, new_head)
        if new_head == self.apple_pos:
            self.eaten = True
            self.update_apple()
        else:
            self.snake.pop(-1)


    def update_apple(self):
        self.eaten = False
        pos = (randint(1, MAX_WIDTH - 1), randint(1, MAX_HEIGHT - 1))
        while pos in self.snake:
            pos = (randint(1, MAX_WIDTH - 1), randint(1, MAX_HEIGHT - 1))
        self.apple_pos = pos
    

    def print_field(self):
        for cell in CELLS:
            if cell in self.snake:
                print('S', end='')
            elif cell[0] in (0, MAX_WIDTH - 1) or cell[1] in (0, MAX_HEIGHT - 1):
                print("#", end='')
                if cell[0] == MAX_WIDTH - 1:
                    print('')
            else:
                if cell == self.apple_pos:
                    print('a', end='')
                else:
                    print(" ", end='')



snake = SnakeGame()

while True:
    print(UP*(MAX_HEIGHT + 2), end=CLEAR)
    snake.print_field()
    snake.update_snake()
    inp, entered = timedInput('press w/a/s/d to move(q to quit):', timeout=0.3)
    if entered:
        match inp:
            case 'w': 
                snake.direction = DIRECTIONS['up']
            case 'a': 
                snake.direction = DIRECTIONS['left']
            case 's': 
                snake.direction = DIRECTIONS['down']
            case 'd': 
                snake.direction = DIRECTIONS['right']
            case 'q':
                exit(0)
