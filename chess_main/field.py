from __future__ import annotations

from chess_main import exceptions
from chess_main import helpers
from typing import TYPE_CHECKING

from chess_main.settings import (
    FIGURE_COLOR,
    BACKS,
    FIGURES_SYMBOLS,
    HALF_SPACE,
    END,
    DIGITS,
)

if TYPE_CHECKING:
    from chess_main.figures import Figure


class GetColor:
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.figure_color = None

    def set_figure_color(self, figure_color: str) -> None:
        """
        Насроить цвет фигуры.
        """
        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        self.figure_color = figure_color

    def set_back_color(self, back_color: str | None) -> None:
        """
        Насроить цвет фона клетки.
        """
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
    """
    Получение готовой отрисованной позиции.
    """

    def figure_symbol_getter(
        self, figure_symbol: str | None, figure_color: str | None
    ) -> str:
        """
        Возвращает 3 символа для отрисовки фигуры или ее отсутсвия.
        """
        if figure_symbol is None:
            return "   "

        if figure_color not in FIGURE_COLOR:
            raise exceptions.FigureColorError
        elif figure_symbol not in FIGURES_SYMBOLS:
            raise exceptions.FigureSymbolError

        return FIGURE_COLOR[figure_color] + f"{HALF_SPACE}{figure_symbol} "

    def back_getter(self, back_color: str) -> str:
        """
        Получение цвета фона из константы BACKS.
        """
        if back_color not in BACKS:
            raise exceptions.BackColorError
        return BACKS[back_color]

    def get_position(self, color: GetColor, figure_symbol: str | None):
        return (
            self.back_getter(color.back_color)
            + self.figure_symbol_getter(figure_symbol, color.figure_color)
            + END
        )


class Field(list):
    def create_new_field(self) -> None:
        for vertical in range(8):
            self.append([])
            for horizontal in range(8):
                cell = create_cell(horizontal, vertical)
                self[vertical].append((cell, None))

    def print_field(self, reverse=False) -> None:
        length = reversed(range(len(self))) if reverse else range(len(self))

        helpers.print_alphabet()
        for index in length:
            print(f" {DIGITS[index]} ", end="")
            print(*map(lambda item: item[0], self[index]), sep="", end="")
            print(f" {DIGITS[index]} ")
        helpers.print_alphabet()


# class ManageFigure:
def add_figure(figure: Figure, field: Field) -> None:
    """
    Добавление фигуры на данное поле по ее координатам.
    """
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
    """
    Удаление фигуры с данного поля по ее координатам.
    """
    field[figure.y_coordinate][figure.x_coordinate] = (
        create_cell(figure.x_coordinate, figure.y_coordinate),
        None,
    )


def create_cell(
    x_coordinate: int,
    y_coordinate: int,
    back_color: str | None = None,
    figure_color: str | None = None,
    figure_symbol: str | None = None,
) -> str:
    """
    Создание клетки.
    """
    if x_coordinate not in range(8) or y_coordinate not in range(8):
        raise IndexError
    color = GetColor(x_coordinate, y_coordinate)
    if not figure_color is None:
        color.set_figure_color(figure_color)
    color.set_back_color(back_color)
    colored_position = GetColoredPosition()
    return colored_position.get_position(color, figure_symbol)


def change_back(
    horizontal: int, vertical: int, field: Field, back_color: str | None = None
) -> None:
    """
    Изменение клетки на текущем поле.
    """
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


# class ManageWays:
def add_figure_ways(horizontal: int, vertical: int, new_field: Field) -> None:
    """
    Добавление на текущее поле клеток для хода данной фигуры.
    """
    current_color = new_field[vertical][horizontal][-1].color

    for coordinates in new_field[vertical][horizontal][-1].move_cells(new_field):
        if coordinates[-1] is None:
            back_color = "green"
        elif coordinates[-1].color == current_color:
            back_color = "blue"
        else:
            back_color = "red"

        change_back(coordinates[0], coordinates[1], new_field, back_color)


def remove_figure_ways(horizontal: int, vertical: int, new_field: Field) -> None:
    """
    Удаление с текущего поля клеток для хода данной фигуры.
    """
    for coordinates in new_field[vertical][horizontal][-1].move_cells(new_field):
        change_back(coordinates[0], coordinates[1], new_field)
