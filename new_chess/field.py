from __future__ import annotations

import exceptions
import helpers
from typing import TYPE_CHECKING

# import figures
from settings import FIGURE_COLOR, BACKS, FIGURES_SYMBOLS, HALF_SPACE, END

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
            + END
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
    def create_new_field(self) -> None:
        for vertical in range(8):
            self.append([])
            for horizontal in range(8):
                cell = create_cell(horizontal, vertical)
                self[vertical].append((cell, None))

    def print_field(self, reverse=False) -> None:
        length = reversed(range(len(self))) if reverse else range(len(self))
        for index in length:
            print(*map(lambda item: item[0], self[index]), sep="")


def create_cell(
    x_coordinate: int,
    y_coordinate: int,
    back_color: str | None = None,
    figure_color: str | None = None,
    figure_symbol: str | None = None,
) -> str:
    color = GetColor(x_coordinate, y_coordinate)
    if not figure_color is None:
        color.set_figure_color(figure_color)
    color.set_back_color(back_color)
    colored_position = GetColoredPosition(color, figure_symbol)
    return colored_position.cell


def add_figure(figure: Figure, field: Field) -> None:
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


def remove_figure(figure: Figure, field: Field) -> None:
    field[figure.y_coordinate][figure.x_coordinate] = (
        create_cell(figure.x_coordinate, figure.y_coordinate),
        None,
    )


def change_back(
    horizontal: int, vertical: int, field: Field, back_color: str | None = None
):
    figure = helpers.create_coordinates_tuple(horizontal, vertical, field)[-1]

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


def attacked_cell(coordinates: tuple, field: Field, enemy_color: str) -> bool:
    result = []
    for line in field:
        for cell in line:
            if (
                not cell[-1] is None
                and enemy_color == cell[-1].color
                and coordinates in cell[-1].attack_cells(field)
            ):
                result.append(cell)

    return bool(result)


def add_figure_ways(horizontal, vertical, new_field: Field) -> None:
    current_color = new_field[vertical][horizontal][-1].color

    for coordinates in new_field[vertical][horizontal][-1].move_cells(new_field):
        if coordinates[-1] is None:
            back_color = "green"
        elif coordinates[-1].color == current_color:
            back_color = "blue"
        else:
            back_color = "red"

        change_back(coordinates[0], coordinates[1], new_field, back_color)


def remove_figure_ways(horizontal, vertical, new_field: Field) -> None:
    for coordinates in new_field[vertical][horizontal][-1].move_cells(new_field):
        change_back(coordinates[0], coordinates[1], new_field)


# field = Field()
# field.create_new_field()
#
# add_figure(figures.Soldier(0, 0, "black"), field)
# field.print_field()
# print()
# field.print_field(reverse=True)

# print(BACKS["white"] + "   " + Style.RESET_ALL)
