import field
import figures
import helpers
import moves
import random

from exceptions import ChooseFigureError
from settings import FIGURE_COLOR


def main():
    # color = random.choice(tuple(FIGURE_COLOR))
    color = "black"

    new_field = field.Field()
    new_field.create_new_field()

    field.add_figure(figures.Rook(3, 5, "white"), new_field)
    field.add_figure(figures.King(3, 6, "black"), new_field)
    # field.add_figure(figures.Soldier(2, 5, "black"), new_field)
    field.add_figure(figures.Rook(0, 6, "black"), new_field)
    # field.add_figure(figures.Soldier(2, 7, "white"), new_field)
    # print(new_field[3][2][-1].attack_cells(new_field))
    # print(new_field[0][0][-1].attack_cells(new_field))
    new_field.print_field()
    print()
    new_field.print_field(reverse=True)
    print()
    # field.add_figure_ways(2, 7, new_field)

    # field.add_figure_ways(0, 6, new_field)
    # print(new_field[5][0][-1].move_cells(new_field))
    new_field.print_field()
    # print()
    # print(
    #     field.attacked_cell(
    #         coordinates=helpers.create_coordinates_tuple(1, 5, new_field),
    #         field=new_field,
    #         enemy_color="black",
    #     )
    # )

    # start
    while True:
        try:
            horizontal, vertical = helpers.choose_cell()
            figure = moves.choose_figure(horizontal, vertical, new_field, color)
            break
        except ChooseFigureError as exc:
            helpers.print_error(str(exc))


# должна быть постоянная проверка на то, что атакуют короля

if __name__ == "__main__":
    main()
