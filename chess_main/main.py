from chess_main import field
from chess_main import figures
from chess_main import helpers
from chess_main import moves

from chess_main.ends_of_game import GameEnd


def main():
    player_color = "white"

    new_field = field.Field()
    new_field.create_new_field()
    figures.place_all_figures(new_field)

    new_field.print_field()

    # start
    while True:
        moves.make_move(new_field, player_color)
        enemy_color = helpers.get_enemy_color(player_color)
        player_color = helpers.change_player_color(player_color)
        try:
            is_end = GameEnd(current_field=new_field, color=enemy_color)
            if is_end.check_all_conditions():
                break
        except IndexError:
            continue


if __name__ == "__main__":
    main()
