# проверка фигуры на то, если она отойдет и будет мат, тогда мы её не можем выбрать и возбуждать исключение
from __future__ import annotations

from chess_main.exceptions import NotFigureError
from chess_main import helpers

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess_main.figures import Figure
    from chess_main.field import Field

BLACK_KING_COORDINATES = (4, 0)
WHITE_KING_COORDINATES = (4, 7)

KING = {"white": WHITE_KING_COORDINATES, "black": BLACK_KING_COORDINATES}


def check_shah(current_field: Field, color: str) -> bool:
    """
    Проверка на шах королю данного цвета.

    :param current_field: текущее поле
    :param color: текущий цвет фигур, в том числе короля
    :return:
    """
    enemy_color = helpers.get_enemy_color(color)
    king = KING[color]
    king_coordinates = helpers.create_coordinates_tuple(
        king[0], king[-1], current_field
    )

    return helpers.attacked_cell(king_coordinates, current_field, enemy_color)


def attacking_figures(
    figure_coordinates: tuple[int, int, Figure | None],
    current_field: Field,
    enemy_color: str,
) -> list:
    """
    Список фигур, атакующих данную позицию.
    """
    result = []

    for vertical, line in enumerate(current_field):
        for horizontal, cell in enumerate(line):
            if (
                not cell[-1] is None
                and enemy_color == cell[-1].color
                and figure_coordinates in cell[-1].move_cells(current_field)
            ):
                result.append(
                    helpers.create_coordinates_tuple(
                        horizontal, vertical, current_field
                    )
                )

    return result


def get_king_coordinates(current_field: Field, color: str) -> tuple[int, int, Figure]:
    """
    Получение координат корля по цвету.
    """
    return helpers.create_coordinates_tuple(*KING[color], current_field)


def change_coordinates(horizontal: int, vertical: int, figure: Figure) -> Figure:
    """
    Изменяет старые координаты фигуры - на новые.
    """
    if figure.__class__.__name__ == "King":
        KING[figure.color] = (horizontal, vertical)

    if horizontal not in range(8) or vertical not in range(8):
        raise IndexError
    if figure is None:
        raise NotFigureError

    figure.x_coordinate = horizontal
    figure.y_coordinate = vertical
    return figure
