from chess_main.field import Field, add_figure
from chess_main.figures import King, Rook, Soldier, Bishop, Knight, Queen
from chess_main.permanent_checkers import change_coordinates, KING
from chess_main.helpers import get_enemy_color


class DoPlacement:
    def __init__(self, color: str, figure_coords: tuple[int, int] | None = None):
        self.color = color
        self.figure = figure_coords

    def get_castling_placement(self, current_field: Field):
        vertical = 7 if self.color == "white" else 0
        add_figure(Rook(0, vertical, self.color), current_field)
        add_figure(King(4, vertical, self.color), current_field)
        add_figure(Rook(7, vertical, self.color), current_field)

    def get_soldier_end_placement(self, current_field: Field):
        if not self.figure is None:
            add_figure(Soldier(*self.figure, self.color), current_field)

    def get_shah_placement(self):
        placements = ShahPlacements(self.color)
        return (
            placements.first_shah_placement,
            placements.second_shah_placement,
            placements.third_shah_placement,
        )


class ShahPlacements:
    def __init__(self, color):
        self.color = color
        self.enemy_color = get_enemy_color(color)

    def change_king_coordinates(self, horizontal, vertical, current_field: Field):
        king = King(horizontal, vertical, self.color)
        add_figure(king, current_field)
        change_coordinates(king.x_coordinate, king.y_coordinate, king)

    def first_shah_placement(self, current_field: Field):
        self.change_king_coordinates(0, 0, current_field)
        add_figure(Bishop(3, 3, "white"), current_field)
        add_figure(Rook(1, 0, "black"), current_field)
        add_figure(Soldier(0, 1, "black"), current_field)

    def second_shah_placement(self, current_field: Field):
        self.change_king_coordinates(2, 0, current_field)
        add_figure(Rook(2, 1, "black"), current_field)
        add_figure(Bishop(1, 0, "white"), current_field)
        add_figure(Rook(3, 0, "white"), current_field)
        add_figure(Knight(4, 2, "white"), current_field)

    def third_shah_placement(self, current_field: Field):
        self.change_king_coordinates(2, 0, current_field)
        add_figure(Soldier(1, 1, "black"), current_field)
        add_figure(Rook(3, 1, "black"), current_field)
        add_figure(Queen(0, 2, "white"), current_field)
        add_figure(Bishop(5, 3, "white"), current_field)
