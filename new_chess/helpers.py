from __future__ import annotations

from typing import TYPE_CHECKING

from settings import ALPHABET, BACKS, END
from exceptions import InputError

if TYPE_CHECKING:
    from figures import Figure
    from field import Field


def create_coordinates_tuple(
    horizontal: int, vertical: int, field: Field
) -> tuple[int, int, Figure]:
    return horizontal, vertical, field[vertical][horizontal][-1]


def get_enemy_color(current_color: str) -> str:
    return "black" if current_color == "white" else "white"


def change_player_color(current_color: str) -> str:
    return get_enemy_color(current_color)


def choose_cell() -> tuple:
    while True:
        try:
            input_coordinates = input("Введие клетку (например: A1): ")

            if not input_coordinates[-1].isdigit():
                raise InputError("Второй символ должен быть цифрой")

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
    print(BACKS["red"] + text + END, end="\n\n")
