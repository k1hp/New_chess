from __future__ import annotations

from dataclasses import dataclass

from chess_main.exceptions import EndOfGame
from chess_main.helpers import print_error, create_coordinates_tuple, get_enemy_color
from chess_main.permanent_checkers import check_shah, KING, attacking_figures, get_king_coordinates
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from chess_main.figures import Figure
    from chess_main.field import Field


class GameEnd:
    def __init__(self, current_field, color):
        self.all_figures = {"black": [], "white": []}
        self.current_field = current_field
        self.current_color = color
        self.enemy_color = get_enemy_color(color)
        for line in current_field:
            for cell in line:
                if hasattr(cell[-1], "color"):
                    self.all_figures[cell[-1].color].append(cell[-1].__class__.__name__)

    def checkmate(self):
        # king_coordinates = create_coordinates_tuple(
        #     *KING[self.current_color], self.current_field
        # )
        king_coordinates = get_king_coordinates(self.current_field, self.current_color)
        king = king_coordinates[-1]
        try:
            attacking_figure = attacking_figures(
                king_coordinates, self.current_field, self.enemy_color
            )[0]
            blocker = Blockers(
                attacking_figure,
                king_coordinates,
                self.current_field,
                self.current_color,
            )
            conditions = (
                check_shah(self.current_field, self.current_color),
                not bool(king.move_cells(self.current_field)),
                not bool(
                    attacking_figures(
                        attacking_figure, self.current_field, self.current_color
                    )
                )
                and not blocker.can_blocked(),  # нельзя перекрыть,
            )
            if all(conditions):
                raise EndOfGame
        except IndexError:
            pass

    def stalemate(self): ...

    def draw(self):
        set_fgs = {"Knight", "Bishop"}
        if len(self.all_figures["black"]) == 1 and len(self.all_figures["white"]) == 1:
            raise EndOfGame("Draw Game")
        if (
            len(self.all_figures["black"]) == 2
            and len(self.all_figures["white"]) == 2
            and set_fgs.intersection(self.all_figures["black"])
            and set_fgs.intersection(self.all_figures["white"])
        ):
            raise EndOfGame("Draw Game")

    def check_all_conditions(self):
        try:
            self.checkmate()
            self.stalemate()
            self.draw()
        except EndOfGame as exc:
            print_error(exc.__str__())
            return "EndOfGame"


@dataclass
class Blockers:
    enemy_figure: tuple[int, int, Figure]
    union_king: tuple[int, int, Figure]
    current_field: Field
    color: str

    @property
    def enemy_name(self):
        return self.enemy_figure[-1].__class__.__name__

    def can_blocked(self):
        if self.enemy_name in ("Soldier", "Knight", "King"):
            return False
        blocked_cells = self.get_blocked_cells()
        return any(
            bool(attacking_figures(cell, self.current_field, self.color))
            for cell in blocked_cells
        )

    def get_blocked_cells(self):
        functions = {
            "Rook": self.get_rook_block,
            "Queen": self.get_queen_block,
            "Bishop": self.get_bishop_block,
        }
        return functions[self.enemy_name]

    def get_rook_block(self) -> list:
        x_coordinate = self.enemy_figure[0]
        y_coordinate = self.enemy_figure[1]
        start_horizontal = 0
        end_horizontal = 7
        start_vertical = 0
        end_vertical = 7
        result = []

        if not (
            self.enemy_figure[0] != self.union_king[0]
            or self.enemy_figure[1] != self.union_king[1]
        ):
            return result

        if ...:
            ...

        return result

    def get_bishop_block(self) -> list:
        # result = []
        # directions = [
        #     (-chess_main, -chess_main),  # верхний левый
        #     (-chess_main, chess_main),  # верхний правый
        #     (chess_main, -chess_main),  # нижний левый
        #     (chess_main, chess_main),  # нижний правый
        # ]
        #
        # for direction in directions:
        #     x, y = self.x_coordinate, self.y_coordinate
        #     while True:
        #         x += direction[0]
        #         y += direction[chess_main]
        #
        #         # Проверяем, не вышли ли мы за пределы доски
        #         if not (0 <= x < len(current_field[0]) and 0 <= y < len(current_field)):
        #             break
        #
        #         figure_coordinates = helpers.create_coordinates_tuple(x, y, current_field)
        #
        #         # Проверяем, не достигли ли мы короля
        #         if (x, y) == (self.king_x_coordinate, self.king_y_coordinate):
        #             break
        #
        #         result.append(figure_coordinates)
        #
        #         # Если ячейка не пустая, прекращаем просмотр
        #         if figure_coordinates[-chess_main] is not None:
        #             break
        #
        # return result
        return []

    def get_queen_block(self) -> list:
        return self.get_rook_block() + self.get_bishop_block()
