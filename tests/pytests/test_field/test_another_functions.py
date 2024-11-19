import pytest

from chess_main.field import create_cell, change_back, attacked_cell
from chess_main.helpers import create_coordinates_tuple
from chess_main.settings import BACKS, END, FIGURE_COLOR, HALF_SPACE

from tests.pytests.conftest import first_figures_placement


@pytest.mark.parametrize(
    "horizontal, vertical, back_color, figure_color, symbol, result",
    [
        (0, 0, "green", None, None, BACKS["green"] + "   " + END),
        (0, 0, "red", None, None, BACKS["red"] + "   " + END),
        (0, 0, "blue", None, None, BACKS["blue"] + "   " + END),
        (4, 4, None, None, None, BACKS["white"] + "   " + END),
        (1, 2, None, None, None, BACKS["black"] + "   " + END),
        (
            1,
            2,
            "black",
            "black",
            "♟",
            BACKS["black"] + FIGURE_COLOR["black"] + f"{HALF_SPACE}♟ " + END,
        ),
        (
            1,
            2,
            "green",
            "white",
            "♚",
            BACKS["green"] + FIGURE_COLOR["white"] + f"{HALF_SPACE}♚ " + END,
        ),
        (
            1,
            2,
            "red",
            "black",
            "♝",
            BACKS["red"] + FIGURE_COLOR["black"] + f"{HALF_SPACE}♝ " + END,
        ),
    ],
)
def test_create_cell(horizontal, vertical, back_color, figure_color, symbol, result):
    assert create_cell(horizontal, vertical, back_color, figure_color, symbol) == result


@pytest.mark.parametrize("horizontal, vertical", [(8, 1), (1, 8), (9, 9)])
def test_create_cell_fail(horizontal, vertical):
    with pytest.raises(IndexError):
        create_cell(horizontal, vertical)


@pytest.mark.parametrize(
    "horizontal, vertical, back_color", [(0, 0, "red"), (1, 1, "green"), (2, 5, "blue")]
)
def test_change_back(horizontal, vertical, back_color, get_start_field):
    start_cell = get_start_field[vertical][horizontal][0]
    change_back(horizontal, vertical, get_start_field, back_color)
    end_cell = get_start_field[vertical][horizontal][0]

    assert end_cell != start_cell
    # запомнить клетку а потом посмотреть изменилась она или нет неважно как потому что мы тестили предыдущуб функцию


placement = first_figures_placement()


@pytest.mark.parametrize(
    "cell_coordinates, enemy_color, result",
    [
        (create_coordinates_tuple(2, 2, placement), "black", True),
        (create_coordinates_tuple(1, 1, placement), "white", False),
    ],
)
def test_attacked_cell(cell_coordinates, enemy_color, result, field=placement):
    print(cell_coordinates[-1].attack_cells(field))
    assert attacked_cell(cell_coordinates, field, enemy_color) == result
