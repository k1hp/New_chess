from colorama import Fore, Back, Style

BLACK_FIGURE = Fore.BLACK
WHITE_FIGURE = Fore.WHITE

FIGURE_COLOR = {"black": BLACK_FIGURE, "white": WHITE_FIGURE}

BACKS = {
    "black": "\033[48;2;29;61;51m",
    "white": "\033[48;2;255;245;220m",
    "green": Back.GREEN,
    "red": Back.RED,
    "blue": Back.BLUE,
}

END = Style.RESET_ALL

HALF_SPACE = "\u2005"

FIGURES_SYMBOLS = "♚♛♜♝♞♟"

ALPHABET = "abcdefgh"

DIGITS = "12345678"

SWAP_FIGURES_NAMES = ("bishop", "knight", "queen", "rook")
