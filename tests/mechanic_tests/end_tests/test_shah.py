import pytest
from unittest.mock import Mock

from tests.mechanic_tests.conftest import basic_actions
from tests.mechanic_tests.placements import DoPlacement
from chess_main import figures


@pytest.mark.parametrize(
    "input_data, color, test_number",
    [
        (["A2", "B1", "B2"], "black", 0),
        # (["H8", "E8"], "white", 0),
    ],
)
def test_shah_brake(input_data, color, test_number):
    placements = DoPlacement(color)
    placement = placements.get_shah_placement()[test_number]

    mock_place_all_figures = Mock(side_effect=placement)
    figures.place_all_figures = mock_place_all_figures

    basic_actions(input_data, color)
