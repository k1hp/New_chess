from __future__ import annotations

from typing import TYPE_CHECKING
from functools import wraps

from chess_main.field import remove_figure, add_figure
from chess_main.permanent_checkers import check_shah
from chess_main.ends_of_game import ShahChecker

if TYPE_CHECKING:
    from chess_main.field import Field
    from chess_main.figures import Figure


# переписать декоратор в класс, когда будет исправлена ошибка
def move_opportunity(function):
    """
    Изменяет поведение функции, которая возвращает клетки для хода.

    :param function: декорируемая функция
    :return: список клеток для хода
    """

    @wraps(function)
    def wrapper(self, current_field: Field) -> list:

        try:
            remove_figure(self, current_field)
            if check_shah(current_field, self.color):
                result = shah_moves(self, current_field, function)
                add_figure(self, current_field)
                return result
            add_figure(self, current_field)
        except IndexError:
            pass

        return function(self, current_field)

    return wrapper


def shah_moves(figure: Figure, current_field: Field, function) -> list:
    """
    Клетки, на которые можно сходить, при шахе королю.
    """
    shah_checker = ShahChecker(current_field, figure.color)
    shah_cells = set(shah_checker.shah_cells())
    result = list(shah_cells.intersection(function(figure, current_field)))
    return result
