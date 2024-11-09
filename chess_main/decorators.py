from __future__ import annotations

from typing import TYPE_CHECKING
from functools import wraps

from chess_main import helpers
from chess_main.field import remove_figure, add_figure
from chess_main.permanent_checkers import check_shah, get_king_coordinates, attacking_figures
from chess_main.ends_of_game import ShahChecker

if TYPE_CHECKING:
    from chess_main.field import Field

# переписать декоратор в класс, когда будет исправлена ошибка
def move_opportunity(function):
    @wraps(function)
    def wrapper(self, current_field: Field) -> list:

        try:
            # if check_shah(current_field, self.color):
            #     shah_checker = ShahChecker(current_field, self.color)
            #     shah_cells = set(shah_checker.shah_cells())
            #     result = list(shah_cells.intersection(function(self, current_field)))
            #     print(result)
            #     return result
            remove_figure(self, current_field)
            if check_shah(current_field, self.color):
                result = shah_moves(self, current_field, function)
                add_figure(self, current_field)
                return result
            add_figure(self, current_field)
        except IndexError:
            print('Errorka')
            pass
            # if enemy_figure in self.attack_cells(current_field):
            #     return [enemy_figure]
        # except IndexError:
        #     print("Атакующих фигур не найдено")

        print("error")
        return function(self, current_field)

    return wrapper

def shah_moves(figure, current_field, function):
    shah_checker = ShahChecker(current_field, figure.color)
    shah_cells = set(shah_checker.shah_cells())
    result = list(shah_cells.intersection(function(figure, current_field)))
    print(result)
    return result