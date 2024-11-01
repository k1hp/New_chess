from __future__ import annotations


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from field import Field


def create_coordinates_tuple(horizontal: int, vertical: int, field: Field):
    return horizontal, vertical, field[vertical][horizontal][-1]
