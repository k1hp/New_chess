from chess_main.field import Field, add_figure
from chess_main.figures import King, Rook


class DoPlacement:
    def __init__(self, *coordinates):
        self.rook_coords = coordinates[0]
        self.king_coords = coordinates[1]

    def get_placement(self, current_field):
        add_figure(Rook(*self.rook_coords, "black"), current_field)
        add_figure(King(*self.king_coords, "black"), current_field)

    def get_shah_placement(self, current_field): ...
