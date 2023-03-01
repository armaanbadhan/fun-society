from sys import stdout


class AnsiCodes:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"

    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

    RESET = "\033c"
    HOME = "\033[;H" + "\r"

    UP = '\033[1A'
    DOWN = '\033[1B'
    FORWARD = '\033[1C'
    BACK = '\033[1D'

    RESET_COLOR = '\033[0m'


def clear_all():
    stdout.write(AnsiCodes.RESET)


def go_down_n(n: int):
    stdout.write(f'\033[{n}B')


def go_right_n(n: int):
    stdout.write(f'\033[{n}C')


# noinspection PyShadowingBuiltins
def print(print_this, *, pos_x: int = -1, pos_y: int = -1, color=None, reset_color: bool = True, blink: bool = False,
          faint: bool = False, bold=False, italic=False, underline=False, negative=False, crossed=False):
    """
    if pos_x or pos_y not given, continue from the cursors position
    if any one given, go home, then go down and/or right
    """
    if pos_x >= 0 or pos_y >= 0:
        stdout.write(AnsiCodes.HOME)
    if pos_y > 0:
        go_down_n(pos_y)
    if pos_x > 0:
        go_right_n(pos_x)

    if color is not None:
        stdout.write(color)
    if blink:
        stdout.write(AnsiCodes.BLINK)
    if faint:
        stdout.write(AnsiCodes.FAINT)
    if bold:
        stdout.write(AnsiCodes.BOLD)
    if italic:
        stdout.write(AnsiCodes.ITALIC)
    if underline:
        stdout.write(AnsiCodes.UNDERLINE)
    if negative:
        stdout.write(AnsiCodes.NEGATIVE)
    if crossed:
        stdout.write(AnsiCodes.CROSSED)
    stdout.write(print_this)
    if reset_color:
        stdout.write(AnsiCodes.RESET_COLOR)
