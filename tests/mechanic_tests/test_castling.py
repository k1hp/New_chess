import pytest
from unittest.mock import Mock, patch


from tests.mechanic_tests.placements import DoPlacement
from chess_main import main
from chess_main import figures
from chess_main.ends_of_game import GameEnd


@pytest.mark.parametrize(
    "inp1, inp2, letter_coords",
    [((0, 0), (4, 0), ["A1", "E1"]), ((7, 0), (4, 0), ["H1", "E1"])],
)
def test_first_castling(inp1, inp2, letter_coords):
    print()
    placements = DoPlacement(inp1, inp2)
    mock_place_all_figures = Mock(side_effect=placements.get_placement)
    figures.place_all_figures = mock_place_all_figures

    mock_check_all_conditions = Mock(return_value=True)

    GameEnd.__init__ = Mock(return_value=None)

    with (
        patch.object(
            GameEnd, "check_all_conditions", side_effect=mock_check_all_conditions
        ),
        patch("builtins.input", side_effect=letter_coords),
    ):
        main.main()
