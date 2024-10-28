import exceptions

from colorama import Style
from settings import FIGURE_COLOR, BACKS, figures


class GetColor:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.figure_color = None

    def set_figure_color(self, figure_color: str):
        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        self.figure_color = figure_color

    def set_back_color(self, back_color: str | None = None):
        if back_color is None:
            if (
                self.x_coordinate % 2 == 0
                and self.y_coordinate % 2 != 0
                or self.x_coordinate % 2 != 0
                and self.y_coordinate % 2 == 0
            ):
                self.back_color = "black"
            else:
                self.back_color = "white"
        else:
            if back_color not in BACKS:
                raise exceptions.BackColorError
            self.back_color = back_color


class GetColoredPosition:
    def __init__(self, color: GetColor, figure_symbol: str | None = None):
        self.cell = (
            self.back_getter(color.back_color)
            + self.figure_symbol_getter(figure_symbol, color.figure_color)
            + Style.RESET_ALL
        )

    def figure_symbol_getter(
        self, figure_symbol: str | None, figure_color: str | None
    ) -> str:
        if figure_symbol is None:
            return "   "

        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        elif figure_symbol not in figures:
            raise exceptions.FigureSymbolError

        return FIGURE_COLOR[figure_color] + f" {figure_symbol} "

    def back_getter(self, back_color: str) -> str:
        if back_color not in BACKS:
            raise exceptions.BackColorError
        return BACKS[back_color]


class Field(list):
    def create_new_field(self):
        for vertical in range(8):
            self.append([])
            for horizontal in range(8):
                color = GetColor(horizontal, vertical)
                color.set_back_color()
                colored_position = GetColoredPosition(color)
                # print(colored_position.cell)
                self[vertical].append(colored_position.cell)

    def print_field(self):
        for index in range(8):
            print(*self[index], sep="")


class AddFigure: ...


class RemoveFigure: ...


field = Field()
field.create_new_field()
field.print_field()


# print(BACKS["white"] + "   " + Style.RESET_ALL)
