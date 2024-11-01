import field
import figures
import helpers


def main():
    new_field = field.Field()
    new_field.create_new_field()

    field.add_figure(figures.King(0, 5, "white"), new_field)
    field.add_figure(figures.King(1, 6, "black"), new_field)
    field.add_figure(figures.Soldier(2, 3, "black"), new_field)
    new_field.print_field()
    print()
    new_field.print_field(reverse=True)
    print(new_field[5][0][-1].move_cells(new_field))
    for coordinates in new_field[5][0][-1].full_check_move(new_field):
        if coordinates[-1] is None:
            back_color = "green"
        else:
            back_color = "red"

        field.change_back(coordinates[0], coordinates[1], new_field, back_color)

    print(new_field[5][0][-1].move_cells(new_field))
    new_field.print_field()
    print()
    print(
        field.attacked_cell(
            coordinates=helpers.create_coordinates_tuple(1, 5, new_field),
            field=new_field,
            figure_color="black",
        )
    )


# должна быть постоянная проверка на то, что атакуют короля

if __name__ == "__main__":
    main()
