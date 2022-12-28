
class Colors:
    """ ANSI color codes """
    # https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
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


class Cursor:
    RESET = "\033c"
    HOME = "\r" + "\033[;H" + "\r"

    UP =      '\033[1A'
    DOWN =    '\033[1B'
    FORWARD = '\033[1C'
    BACK =    '\033[1D'

    CLEAR = '\033[2K'
    GO_TO_START_OF_LINE = "\r"


    UNDERLINE = "\033[4m"
    RED = '\033[0;31m'
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_BLUE = '\033[1;34m'
    RESET_COLOR = '\033[0m'

