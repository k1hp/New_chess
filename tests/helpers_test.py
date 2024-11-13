import unittest

# sys.path.append(os.path.join(os.getcwd(), "../chess_main"))
from chess_main import helpers
from chess_main.exceptions import ColorError, NotFigureError
from chess_main.field import Field
from chess_main.figures import place_all_figures
from chess_main.figures import Soldier


class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.new_field = Field()
        self.new_field.create_new_field()
        place_all_figures(self.new_field)

    def test_get_enemy_color(self):
        self.assertEqual(helpers.get_enemy_color("white"), "black")
        with self.assertRaises(ColorError):
            self.assertEqual(helpers.get_enemy_color("blue"), "")

    def test_create_coordinates_tuple(self):
        self.assertEqual(
            helpers.create_coordinates_tuple(0, 0, self.new_field),
            (0, 0, self.new_field[0][0][-1]),
        )
        self.assertEqual(
            helpers.create_coordinates_tuple(2, 0, self.new_field),
            (2, 0, self.new_field[0][2][-1]),
        )
        with self.assertRaises(IndexError):
            self.assertEqual(
                helpers.create_coordinates_tuple(10, 0, self.new_field),
                (0, 10, self.new_field[10][0][-1]),
            )

    def test_change_coordinates(self):
        first_figure = Soldier(0, 0, "black")
        second_figure = None
        true_figure = Soldier(6, 2, "black")

        first_figure = helpers.change_coordinates(6, 2, first_figure)
        figure_coordinates = first_figure.x_coordinate, first_figure.y_coordinate
        edit_figure_coordinates = true_figure.x_coordinate, true_figure.y_coordinate
        self.assertEqual(figure_coordinates, edit_figure_coordinates)

        with self.assertRaises(IndexError):
            first_figure = helpers.change_coordinates(9, 2, first_figure)

        with self.assertRaises(NotFigureError):
            second_figure = helpers.change_coordinates(6, 2, second_figure)

    def test_change_player_color(self):
        self.assertEqual(helpers.change_player_color("white"), "black")
        with self.assertRaises(ColorError):
            self.assertEqual(helpers.change_player_color("blue"), "")

    def test_(self): ... # надо юзать моки from unittest import mock что-то такое


if __name__ == "__main__":
    unittest.main()