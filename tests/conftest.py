import pytest
from chess_main.field import Field, add_figure
from chess_main.figures import place_all_figures, Rook, Bishop, Soldier


def create_field():
    field = Field()
    field.create_new_field()
    return field


@pytest.fixture
def get_start_field():
    field = create_field()
    place_all_figures(field)
    return field


def first_figures_placement():
    field = create_field()
    add_figure(Rook(2, 2, "white"), field)
    add_figure(Soldier(1, 1, "black"), field)
    return field


@pytest.fixture
def second_figures_placement():
    field = create_field()
    add_figure(Soldier(5, 6, "white"), field)
    add_figure(Soldier(3, 1, "black"), field)
    add_figure(Rook(4, 3, "black"), field)
    return field
