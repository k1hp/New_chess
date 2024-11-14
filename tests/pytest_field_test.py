import pytest

from chess_main.exceptions import BackColorError, FigureColorError
from chess_main.field import GetColor


@pytest.mark.parametrize(
    "horizontal, vertical, back_color, result",
    [
        (0, 0, None, "white"),
        (0, 1, "white", "white"),
        (1, 0, "black", "black"),
        (1, 1, "blue", "blue"),
        (1, 2, "yellow", "yellow"),
    ],
)
def test_GetColor_set_back(horizontal, vertical, back_color, result):
    color = GetColor(horizontal, vertical)
    color.set_back_color(back_color)
    assert color.back_color == result


@pytest.mark.parametrize(
    "horizontal, vertical, back_color, result",
    [
        (1, 2, "yellow", "yellow"),
        (2, 4, "faufdai", "3fda"),
        (2, 3, "1234565", "1234565"),
    ],
)
def test_GetColor_set_back_fail(horizontal, vertical, back_color, result):
    with pytest.raises(BackColorError) as exc:
        color = GetColor(horizontal, vertical)
        color.set_back_color(back_color)
    print(exc)


@pytest.mark.parametrize(
    "horizontal, vertical, figure_color, result",
    [
        (1, 2, "black", "black"),
        (2, 4, "white", "white"),
        (2, 3, "red", "red"),
        (7, 4, "green", "green"),
    ],
)
def test_GetColor_set_figure(horizontal, vertical, figure_color, result):
    color = GetColor(horizontal, vertical)
    color.set_figure_color(figure_color)
    assert color.figure_color == result


@pytest.mark.parametrize(
    "horizontal, vertical, figure_color, result",
    [
        (0, 0, None, None),
        (1, 2, "yellow", "yellow"),
        (2, 4, "blue", "blue"),
        (2, 3, "red", "red"),
        (7, 4, "green", "green"),
    ],
)
def test_GetColor_set_figure_fail(horizontal, vertical, figure_color, result):
    with pytest.raises(FigureColorError) as exc:
        color = GetColor(horizontal, vertical)
        color.set_figure_color(figure_color)
    print(exc)
