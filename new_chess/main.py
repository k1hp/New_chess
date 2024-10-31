import field
import figures


def main():
    new_field = field.Field()
    new_field.create_new_field()

    field.add_figure(figures.Soldier(0, 5, "black"), new_field)
    field.add_figure(figures.Soldier(1, 6, "white"), new_field)
    new_field.print_field()
    print()
    new_field.print_field(reverse=True)
    print(new_field[5][0][-1].move_cells(new_field))
    for coordinates in new_field[5][0][-1].move_cells(new_field):
        if coordinates[-1] is None:
            back_color = "green"
        else:
            back_color = "red"

        field.change_back(coordinates[0], coordinates[1], new_field, back_color)

    print(new_field[5][0][-1].move_cells(new_field))
    new_field.print_field()


if __name__ == "__main__":
    main()
