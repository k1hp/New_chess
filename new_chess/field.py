import exceptions

from colorama import Fore, Back, Style
from settings import FIGURE_COLOR



class Colors:
    def total_getter(self, figure_symbol: str = None, figure_color: str = None):
        if figure_symbol is None:
            return ''
        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        elif figure_symbol not in settings.figures:
            raise exceptions.FigureSymbolError
        return FIGURE_COLOR[figure_color] + f' {} '

    def get_white(self, symbol):
        WHITE_COLOR = Back.WHITE + f" {self.symbol} " + Style.RESET_ALL
        BLACK_COLOR = Back.GREEN + "   " + Style.RESET_ALL
        CAN_MOVE = ...
        CAN_KILL = ...


class GetColoredPosition:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = Colors()
        ...


# class PrintColoredPosition:
#     def __init__(
#         self, x_coordinate: int, y_coordinate: int, colored_position: GetColoredPosition
#     ):
#         self.x_coordinate = x_coordinate
#         self.y_coordinate = y_coordinate
#         self.colored_position = colored_position


class Field(list):
    def create_new_field(self):
        for vertical in range(8):
            self.append([GetColoredPosition() for gorizontal in range(8)])

    def print_field(self):
        for index in range(8):
            print(*self[index])


field = Field()
field.create_new_field()
field.print_field()
