from __future__ import annotations

from typing import TYPE_CHECKING

from chess_main.settings import ALPHABET, BACKS, END, FIGURE_COLOR
from chess_main.exceptions import InputError, ColorError, NotFigureError
from chess_main.permanent_checkers import KING

if TYPE_CHECKING:
    from chess_main.figures import Figure
    from chess_main.field import Field


def create_coordinates_tuple(
        horizontal: int, vertical: int, field: Field
) -> tuple[int, int, Figure]:
    """
    Из координат создает кортеж, который используется далее.
    """
    return horizontal, vertical, field[vertical][horizontal][-1]


def change_coordinates(horizontal: int, vertical: int, figure: Figure) -> Figure:
    """
    Изменяет старые координаты фигуры - на новые.
    """
    if figure.__class__.__name__ == "King":
        KING[figure.color] = (horizontal, vertical)

    if horizontal not in range(8) or vertical not in range(8):
        raise IndexError
    if figure is None:
        raise NotFigureError

    figure.x_coordinate = horizontal
    figure.y_coordinate = vertical
    return figure


def get_enemy_color(current_color: str) -> str:
    """
    Возврщает вражеский цвет.

    >>> "white"
    "black"
    """
    if current_color not in FIGURE_COLOR:
        raise ColorError
    return "black" if current_color == "white" else "white"


def change_player_color(current_color: str) -> str:
    """
    Изменение цвета.

    >>> "white"
    "black"
    """
    return get_enemy_color(current_color)


def choose_cell() -> tuple[int, int]:
    """
    Выбор клетки на поле.

    Различные проверки входных данных в бесконечном цикле,
    пока не будет введена корректная клетка, например: A1.

    :return кортеж -> (horizontal, vertical)
    """
    while True:
        try:
            input_coordinates = input("Введие клетку (например: A1): ")

            if not input_coordinates[-1].isdigit():
                raise InputError("Первый символ - буква, а второй - цифра")

            letter = input_coordinates[0].lower()
            vertical = int(input_coordinates[-1]) - 1

            if letter not in ALPHABET:
                raise InputError("Неверно указана буква")
            elif vertical not in range(8):
                raise InputError("Неверно указана цифра")

        except InputError as exc:
            print_error(str(exc))

        else:
            horizontal = ALPHABET.index(letter)
            return horizontal, vertical


def print_error(text: str) -> None:
    """
    Вывод сообщения ошибки на экран.

    Можно залогировать.
    """
    print(BACKS["red"] + text + END, end="\n\n")


def print_alphabet() -> None:
    """
    Выводит набор букв.

    Используется только для отрисовки поля.
    """
    print("   ", end="")
    print(*map(lambda letter: f" {letter.upper()} ", ALPHABET), sep="")
