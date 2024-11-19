# import pytest
# from chess_main import figures
# from tests.mechanic_tests.placements import DoPlacement
#
#
# @pytest.fixture
# def basic_actions():
#     print()
#     placements = DoPlacement(inp1, inp2)
#     mock_place_all_figures = Mock(side_effect=placements.get_placement)
#     figures.place_all_figures = mock_place_all_figures
#
#     mock_check_all_conditions = Mock(return_value=True)
#
#     GameEnd.__init__ = Mock(return_value=None)
#
#     with (
#         patch.object(
#             GameEnd, "check_all_conditions", side_effect=mock_check_all_conditions
#         ),
#         patch("builtins.input", side_effect=letter_coords),
#     ):
#         main.main()
