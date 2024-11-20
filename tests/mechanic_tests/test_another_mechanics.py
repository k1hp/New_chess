import pytest
from unittest.mock import Mock

from tests.mechanic_tests.conftest import basic_actions
from tests.mechanic_tests.placements import DoPlacement
from chess_main import figures


@pytest.mark.parametrize(
    "input_data, color",
    [
        (["A8", "E8"], "white"),
        (["H8", "E8"], "white"),
        (["H1", "E1"], "black"),
        (["A1", "E1"], "black"),
    ],
)
def test_castling(input_data, color):
    placements = DoPlacement(color)
    mock_place_all_figures = Mock(side_effect=placements.get_castling_placement)
    figures.place_all_figures = mock_place_all_figures

    basic_actions(input_data, color)


@pytest.mark.parametrize(
    "input_data, color, coords",
    [
        (["C8", "queen"], "black", (2, 7)),
        (["b1", "bishop"], "white", (1, 0)),
        (["e8", "knight"], "black", (4, 7)),
        (["H1", "rook"], "white", (7, 0)),
    ],
)
def test_replace_soldier(input_data, color, coords):
    placements = DoPlacement(color, coords)
    mock_place_all_figures = Mock(side_effect=placements.get_soldier_end_placement)
    figures.place_all_figures = mock_place_all_figures

    basic_actions(input_data, color)
