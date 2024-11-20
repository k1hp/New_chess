from unittest.mock import Mock, patch

from chess_main import main
from chess_main.ends_of_game import GameEnd


def basic_actions(input_data, color):
    GameEnd.__init__ = Mock(return_value=None)

    print()
    with (
        patch("chess_main.helpers.get_start_color", return_value=color),
        patch.object(GameEnd, "check_all_conditions", return_value=True),
        patch("builtins.input", side_effect=input_data),
    ):
        main.main()
