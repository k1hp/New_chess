from __future__ import annotations

import exceptions
from typing import TYPE_CHECKING

# import figures
from settings import FIGURE_COLOR, BACKS, FIGURES_SYMBOLS, HALF_SPACE

from colorama import Style

if TYPE_CHECKING:
    from figures import Figure


class GetColor:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.figure_color = None

    def set_figure_color(self, figure_color: str):
        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        self.figure_color = figure_color

    def set_back_color(self, back_color: str | None):
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
    def __init__(self, color: GetColor, figure_symbol: str | None):
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
        elif figure_symbol not in FIGURES_SYMBOLS:
            raise exceptions.FigureSymbolError

        return FIGURE_COLOR[figure_color] + f"{HALF_SPACE}{figure_symbol} "

    def back_getter(self, back_color: str) -> str:
        if back_color not in BACKS:
            raise exceptions.BackColorError
        return BACKS[back_color]


class Field(list):
    def create_new_field(self):
        for vertical in range(8):
            self.append([])
            for horizontal in range(8):
                cell = create_cell(horizontal, vertical)
                # color = GetColor(horizontal, vertical)
                # color.set_back_color()
                # colored_position = GetColoredPosition(color)
                self[vertical].append((cell, None))

    def print_field(self, reverse=False):
        length = reversed(range(len(self))) if reverse else range(len(self))
        for index in length:
            print(*map(lambda item: item[0], self[index]), sep="")


def create_cell(
    x_coordinate: int,
    y_coordinate: int,
    back_color: str | None = None,
    figure_color: str | None = None,
    figure_symbol: str | None = None,
):
    color = GetColor(x_coordinate, y_coordinate)
    if not figure_color is None:
        color.set_figure_color(figure_color)
    color.set_back_color(back_color)
    colored_position = GetColoredPosition(color, figure_symbol)
    return colored_position.cell


def add_figure(
    figure: Figure, field: Field
):  # проблема с импортом Figure при типизации
    field[figure.y_coordinate][figure.x_coordinate] = (
        create_cell(
            figure.x_coordinate,
            figure.y_coordinate,
            None,
            figure.color,
            figure.symbol,
        ),
        figure,
    )


def change_back(
    horizontal: int, vertical: int, field: Field, back_color: str | None = None
):
    figure = field[horizontal][vertical][-1]

    field[vertical][horizontal] = (
        create_cell(
            horizontal,
            vertical,
            back_color,
            None if figure is None else figure.color,
            None if figure is None else figure.symbol,
        ),
        figure,
    )


class RemoveFigure: ...


# field = Field()
# field.create_new_field()
#
# add_figure(figures.Soldier(0, 0, "black"), field)
# field.print_field()
# print()
# field.print_field(reverse=True)

# print(BACKS["white"] + "   " + Style.RESET_ALL)
