# проверка фигуры на то, если она отойдет и будет мат, тогда мы её не можем выбрать и возбуждать исключение
from __future__ import annotations

from chess_main.field import attacked_cell, Field, remove_figure, add_figure
# from functools import wraps
from chess_main import helpers
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess_main.figures import Figure
    from chess_main.field import Field


BLACK_KING_COORDINATES = (4, 0)
WHITE_KING_COORDINATES = (4, 7)

KING = {"white": WHITE_KING_COORDINATES, "black": BLACK_KING_COORDINATES}


def check_shah(current_field: Field, color: str) -> bool:
    enemy_color = helpers.get_enemy_color(color)
    king = KING[color]
    king_coordinates = helpers.create_coordinates_tuple(
        king[0], king[-1], current_field
    )

    return attacked_cell(king_coordinates, current_field, enemy_color)



# def move_opportunity(function):
#     @wraps(function)
#     def wrapper(self, current_field: Field) -> list:
#         try:
#             king_coordinates = get_king_coordinates(current_field, self.color)
#             enemy_figure = attacking_figures(
#                 king_coordinates, current_field, helpers.get_enemy_color(self.color)
#             )[0]
#             if enemy_figure in self.attack_cells(current_field):
#                 return [enemy_figure]
#         except IndexError:
#             print("Атакующих фигур не найдено")
#
#         remove_figure(self, current_field)
#         result = check_shah(current_field, self.color)
#         add_figure(self, current_field)
#         if result:
#             return []
#         return function(self, current_field)
#
#     return wrapper


def attacking_figures(
    figure_coordinates: tuple[int, int, Figure | None],
    current_field: Field,
    enemy_color: str,
) -> list:
    result = []

    for vertical, line in enumerate(current_field):
        for horizontal, cell in enumerate(line):
            if (
                not cell[-1] is None
                and enemy_color == cell[-1].color
                and figure_coordinates in cell[-1].attack_cells(current_field)
            ):
                result.append(
                    helpers.create_coordinates_tuple(
                        horizontal, vertical, current_field
                    )
                )

    return result


def get_king_coordinates(current_field: Field, color: str) -> tuple[int, int, Figure]:
    return helpers.create_coordinates_tuple(*KING[color], current_field)
