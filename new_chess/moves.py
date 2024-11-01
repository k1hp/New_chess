import field
import settings
from exceptions import ChooseFigureError


def choose_figure(
    horizontal: int, vertical: int, current_field: field.Field, current_color: str
):
    cell = current_field[vertical][horizontal]

    if cell[-1] is None:
        raise ChooseFigureError("На выбранном поле отсутствует фигура")
    elif cell[-1].color != current_color:
        raise ChooseFigureError("Выбранная фигура не вашего цвета")
    elif cell[-1].move_cells(current_field) == []:
        raise ChooseFigureError("Выбранная фигура не может ходить")
    else:
        pass

    field.add_figure_ways(horizontal, vertical, current_field)
    current_field.print_field()


def move(): ...


# если None то просто ходим
# если figure color == current значит это король и мы направляем в castling
# если figure color != current значит направляем в kill
# если исключение EndOfField значит это пешка replace_soldier


def kill(): ...


def replace_soldier(): ...


def castling():  # у лодьи и короля атрибут moved = True
    # castling - рокировка
    ...
