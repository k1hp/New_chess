from chess_main.field import Field, add_figure
from chess_main.figures import King, Rook, Soldier


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

    def get_shah_placement(self, current_field): ...
