# проверка фигуры на то, если она отойдет и будет мат, тогда мы её не можем выбрать и возбуждать исключение
from field import attacked_cell, Field
import helpers


BLACK_KING_COORDINATES = ...
WHITE_KING_COORDINATES = ...

KING = {"white": WHITE_KING_COORDINATES, "black": BLACK_KING_COORDINATES}


def check_shah(current_field: Field, color: str) -> bool:
    enemy_color = helpers.get_enemy_color(color)
    king_coordinates = KING[color]

    return attacked_cell(king_coordinates, current_field, enemy_color)
