import pytest
from unittest.mock import Mock
import builtins

from chess_main.settings import ALPHABET
from chess_main.exceptions import InputError, ColorError
from chess_main.helpers import create_coordinates_tuple, get_enemy_color


def choose_cell_without_loop():
    """
    Код функции choose_cell, но вне цикла.

    Используется только для тестирования.
    """
    try:
        input_coordinates = input("Введие клетку (например: A1): ")

        if len(input_coordinates) != 2:
            raise InputError("Должно быть передано два символа")

        if not input_coordinates[-1].isdigit():
            raise InputError("Первый символ - буква, а второй - цифра")

        letter = input_coordinates[0].lower()
        vertical = int(input_coordinates[-1]) - 1

        if letter not in ALPHABET:
            raise InputError("Неверно указана буква")
        elif vertical not in range(8):
            raise InputError("Неверно указана цифра")

    except InputError:
        raise  # to check exception

    else:
        horizontal = ALPHABET.index(letter)
        return horizontal, vertical


@pytest.mark.parametrize(
    "inp, out", [("a1", (0, 0)), ("c2", (2, 1)), ("g3", (6, 2)), ("a4", (0, 3))]
)
def test_choose_cell(inp, out):
    mock_input = Mock(return_value=inp)
    default_input = builtins.input
    builtins.input = mock_input

    try:
        assert choose_cell_without_loop() == out
    finally:
        builtins.input = default_input


@pytest.mark.parametrize("inp", [("af1",), ("aa",), ("1a",), ("j1",), ("b9",), ("j1",)])
def test_choose_cell_fail(inp):
    mock_input = Mock(return_value=inp)
    default_input = builtins.input
    builtins.input = mock_input

    with pytest.raises(InputError):
        choose_cell_without_loop()

    builtins.input = default_input


@pytest.mark.parametrize(
    "horizontal, vertical, result",
    [
        (0, 0, "Rook"),
        (4, 3, "NoneType"),
        (0, 1, "Soldier"),
        (7, 7, "Rook"),
        (6, 7, "Knight"),
        (2, 7, "Bishop"),
        (3, 0, "Queen"),
        (4, 7, "King"),
    ],
)
def test_create_coordinates_tuple(horizontal, vertical, result, get_start_field):
    created_tuple = create_coordinates_tuple(horizontal, vertical, get_start_field)
    name_figure = created_tuple[-1].__class__.__name__
    assert name_figure == result


@pytest.mark.parametrize("inp, out", [("white", "black"), ("black", "white")])
def test_get_enemy_color(inp, out):
    assert get_enemy_color(inp) == out


@pytest.mark.parametrize(
    "inp, out", [("blue", "black"), ("green", "black"), ("red", "black")]
)
def test_get_enemy_color_fail(inp, out):
    with pytest.raises(ColorError):
        get_enemy_color(inp)
