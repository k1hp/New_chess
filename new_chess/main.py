import field
import figures
import helpers
import moves
import random

from exceptions import ChooseFigureError
from settings import FIGURE_COLOR


def main():
    # player_color = random.choice(tuple(FIGURE_COLOR))
    player_color = "black"

    new_field = field.Field()
    new_field.create_new_field()

    field.add_figure(figures.Rook(5, 5, "white"), new_field)
    field.add_figure(figures.King(4, 6, "black"), new_field)
    field.add_figure(figures.Rook(0, 6, "black"), new_field)
    field.add_figure(figures.Soldier(3, 7, "black"), new_field)
    new_field.print_field()
    print()
    new_field.print_field(reverse=True)
    print()

    # start
    while True:
        moves.make_move(new_field, player_color)
        helpers.change_player_color(player_color)


# должна быть постоянная проверка на то, что атакуют короля

if __name__ == "__main__":
    main()
# в конце нужно написать тесты
