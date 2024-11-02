import field
import settings
from exceptions import ChooseFigureError, EndOfField
import helpers
from figures import Soldier, SWAP_FIGURES, Figure


class Parent:
    def __init__(
        self,
        horizontal: int,
        vertical: int,
        current_field: field.Field,
        current_color: str,
    ):
        self.color = current_color
        self.horizontal = horizontal
        self.vertical = vertical
        self.field = current_field
        self.figure = current_field[vertical][horizontal][-1]

    @property
    def parameters_set(self):
        return self.horizontal, self.vertical, self.field


class Moves(Parent):
    def __init__(self, *args):
        super().__init__(*args)
        self.action = Actions(*args)

    def figure_ways(self):

        if self.figure is None:
            raise ChooseFigureError("На выбранном поле отсутствует фигура")
        elif self.figure.color != self.color:
            raise ChooseFigureError("Выбранная фигура не вашего цвета")
        elif isinstance(self.figure, Soldier) and self.vertical in (0, 7):
            raise EndOfField
        elif self.figure.move_cells(self.field) == []:
            raise ChooseFigureError("Выбранная фигура не может ходить")
        else:
            pass

        field.add_figure_ways(*self.parameters_set)
        self.field.print_field()
        field.remove_figure_ways(*self.parameters_set)

    def make_action(self, guiding_coordinates: tuple[int, int, Figure]) -> None:
        attacked_figure = guiding_coordinates[-1]

        if attacked_figure is None or self.color != attacked_figure.color:
            self.action.relocate(guiding_coordinates)

        elif self.color == attacked_figure.color:
            self.action.castling(guiding_coordinates)
            # вызов castling

    # если None то просто ходим
    # если figure color == current значит это король и мы направляем в castling
    # если figure color != current значит направляем в kill
    # если исключение EndOfField значит это пешка replace_soldier


class Actions(Parent):

    def replace_soldier(self) -> None:
        figure_class = SWAP_FIGURES[
            input(
                "Введите название фигуры, на которую хотите заменить пешку (rook, knight, queen, bishop): "
            ).lower()
        ]
        figure = figure_class(self.horizontal, self.vertical, self.color)
        field.add_figure(figure, self.field)

    def relocate(self, guiding_coordinates: tuple[int, int, Figure]) -> None:
        field.remove_figure(self.figure, self.field)
        self.figure.x_coordinate, self.figure.y_coordinate = guiding_coordinates[0:2]
        field.add_figure(self.figure, self.field)

    def castling(self, king_coordinates: tuple[int, int, Figure]) -> None:
        horizontal = king_coordinates[0]
        king = king_coordinates[-1]
        field.remove_figure(self.figure, self.field)
        field.remove_figure(king, self.field)

        if horizontal < self.figure.x_coordinate:
            self.figure.x_coordinate, horizontal = (
                horizontal + 1,
                self.figure.x_coordinate - 1,
            )
        else:
            self.figure.x_coordinate, horizontal = (
                horizontal - 1,
                self.figure.x_coordinate + 2,
            )

        field.add_figure(self.figure, self.field)
        helpers.change_coordinates(horizontal, self.figure.y_coordinate, king)
        field.add_figure(king, self.field)


def make_move(current_field: field.Field, color: str) -> None:
    while True:
        try:
            horizontal, vertical = helpers.choose_cell()
            move = Moves(horizontal, vertical, current_field, color)
            move.figure_ways()
            current_field.print_field()
        except ChooseFigureError as exc:
            helpers.print_error(str(exc))
        except EndOfField:
            action = Actions(horizontal, vertical, current_field, color)
            action.replace_soldier()
            break
        else:
            while True:
                horizontal, vertical = helpers.choose_cell()
                coordinates = helpers.create_coordinates_tuple(
                    horizontal, vertical, current_field
                )
                if coordinates in move.figure.move_cells(current_field):
                    break

            move.make_action(guiding_coordinates=coordinates)
            break

    print()
    current_field.print_field()
