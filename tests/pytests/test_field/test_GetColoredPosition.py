import pytest

from chess_main.settings import FIGURE_COLOR, HALF_SPACE
from chess_main.exceptions import FigureColorError, FigureSymbolError
from chess_main.field import GetColoredPosition


@pytest.mark.parametrize(
    "color, symbol, result",
    [
        (None, None, "   "),
        (None, "black", "   "),
        ("♚", "black", FIGURE_COLOR["black"] + f"{HALF_SPACE}{"♚"} "),
        ("♟", "white", FIGURE_COLOR["white"] + f"{HALF_SPACE}{"♟"} "),
    ],
)
def test_figure_symbol_getter(color, symbol, result):
    figure = GetColoredPosition()
    assert figure.figure_symbol_getter(symbol, color) == result


@pytest.mark.development
@pytest.mark.parametrize(
    "color, symbol, result",
    [
        ("blue", "♚", " "),
        ("green", "♚", " "),
        ("black", "_", " "),
        ("white", "?", " "),
    ],
)
def test_figure_symbol_getter_fail(color, symbol, result):
    figure = GetColoredPosition()
    with pytest.raises((FigureColorError, FigureSymbolError)):
        figure.figure_symbol_getter(symbol, color)


@pytest.mark.skip(
    reason="Нет смысла проверять, потому что это проверяется в create_cell"
)
def test_get_position(): ...
