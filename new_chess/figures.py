from abc import ABC, abstractmethod

from settings import FIGURE_COLOR, SWAP_FIGURES_NAMES
import exceptions
import field
import helpers


class Figure(ABC):
    def __init__(self, x_coordinate: int, y_coordinate: int, color: str):
        if color not in FIGURE_COLOR:
            raise exceptions.FigureColorError

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color

    @abstractmethod
    def move_cells(self, current_field: field.Field) -> list: ...

    @abstractmethod
    def attack_cells(self, current_field: field.Field) -> list: ...


class Soldier(Figure):
    symbol = "♟"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moved = False

    # def move_cells(self, field: field.Field):
    #     return super().move_cells(field)

    def move_cells(self, current_field: field.Field) -> list:
        result = []

        start = (
            self.x_coordinate if self.x_coordinate - 1 < 0 else self.x_coordinate - 1
        )
        end = self.x_coordinate if self.x_coordinate + 1 > 7 else self.x_coordinate + 1
        vertical = self.get_vertical()  # exceptions.EndOfField
        braker = False

        for horizontal, cell in enumerate(
            current_field[vertical][start : end + 1], start=start
        ):
            if cell[-1] is None and horizontal == self.x_coordinate:
                result.append((horizontal, vertical, None))
            elif cell[-1] is None:
                continue
            elif cell[-1].x_coordinate == self.x_coordinate:
                braker = True
            elif cell[-1].color != self.color:
                result.append((horizontal, vertical, cell[-1]))

        if (
            not self.moved
            and not braker
            and current_field[self.get_vertical(action=1)][self.x_coordinate - 1][-1]
            is None
        ):
            result.append((self.x_coordinate, self.get_vertical(action=1), None))

        return result

    def get_vertical(self, action: int = 0) -> int:
        if self.color == "black":
            result = self.y_coordinate + 1 + action
        else:
            result = self.y_coordinate - 1 - action

        if result in range(8):
            return result
        raise exceptions.EndOfField

    def attack_cells(self, current_field: field.Field) -> list:
        result = []
        left = None if self.x_coordinate - 1 < 0 else self.x_coordinate - 1
        right = None if self.x_coordinate + 1 > 7 else self.x_coordinate + 1
        vertical = self.get_vertical()
        for horizontal in (left, right):
            if not horizontal is None:
                result.append(
                    helpers.create_coordinates_tuple(
                        horizontal, vertical, current_field
                    )
                )
        return result


class King(Figure):
    symbol = "♚"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moved = False

    def move_cells(self, current_field: field.Field) -> list:
        result = []
        for vertical, line in enumerate(current_field):
            result.extend(
                (horizontal, vertical, cell[-1])
                for horizontal, cell in enumerate(line)
                if abs(horizontal - self.x_coordinate) <= 1
                and abs(vertical - self.y_coordinate) <= 1
                and not (
                    horizontal == self.x_coordinate and vertical == self.y_coordinate
                )
                and (True if cell[-1] is None else cell[-1].color != self.color)
            )

        return self.full_check_move(current_field, result)

    def full_check_move(self, current_field: field.Field, result: list = None) -> list:
        if result is None:
            result = []

        return list(
            filter(
                lambda coordinates: (
                    not field.attacked_cell(
                        coordinates, current_field, helpers.get_enemy_color(self.color)
                    )
                ),
                result,
            )
        )

    def attack_cells(self, current_field: field.Field) -> list:
        result = []
        for vertical, line in enumerate(current_field):
            result.extend(
                helpers.create_coordinates_tuple(horizontal, vertical, current_field)
                for horizontal, cell in enumerate(line)
                if abs(horizontal - self.x_coordinate) <= 1
                and abs(vertical - self.y_coordinate) <= 1
                and not (
                    horizontal == self.x_coordinate and vertical == self.y_coordinate
                )
            )

        return result


class Rook(Figure):
    symbol = "♜"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moved = False

    def move_cells(self, current_field: field.Field) -> list:
        # attack_cells исключаем фигуры такого же цвета как self.color
        return list(
            filter(
                lambda coordinates: (
                    True
                    if coordinates[-1] is None
                    else coordinates[-1].color != self.color
                    or (
                        isinstance(coordinates[-1], King)
                        and coordinates[-1].color == self.color
                        and self.can_castling(current_field)
                    )
                ),
                self.attack_cells(current_field),
            )
        )

    def attack_cells(self, current_field: field.Field) -> list:
        start_horizontal = 0
        end_horizontal = 7
        start_vertical = 0
        end_vertical = 7
        result = []

        for vertical, line in enumerate(current_field):
            if (
                not line[self.x_coordinate][-1] is None
                and start_vertical < vertical < self.y_coordinate
            ):
                start_vertical = vertical
            elif (
                not line[self.x_coordinate][-1] is None
                and end_vertical > vertical > self.y_coordinate
            ):
                end_vertical = vertical

            if vertical == self.y_coordinate:
                for horizontal, cell in enumerate(line):
                    if (
                        not cell[-1] is None
                        and start_horizontal < horizontal < self.x_coordinate
                    ):
                        start_horizontal = horizontal
                    elif (
                        not cell[-1] is None
                        and end_horizontal > horizontal > self.x_coordinate
                    ):
                        end_horizontal = horizontal

        for horizontal in range(start_horizontal, end_horizontal + 1):
            if horizontal != self.x_coordinate:
                result.append(
                    helpers.create_coordinates_tuple(
                        horizontal, self.y_coordinate, current_field
                    )
                )

        for vertical in range(start_vertical, end_vertical + 1):
            if vertical != self.y_coordinate:
                result.append(
                    helpers.create_coordinates_tuple(
                        self.x_coordinate, vertical, current_field
                    )
                )

        return result

    def can_castling(self, current_field: field.Field) -> bool:

        try:
            king = next(
                filter(
                    lambda coordinates: isinstance(coordinates[-1], King)
                    and coordinates[-1].color == self.color,
                    self.attack_cells(current_field),
                )
            )
        except StopIteration:
            return False

        interval = (
            range(self.x_coordinate + 1, king[0] + 1)
            if king[0] > self.x_coordinate
            else range(king[0], self.x_coordinate)
        )
        enemy_color = helpers.get_enemy_color(self.color)
        vertical = self.y_coordinate

        for horizontal in interval:
            coordinates = helpers.create_coordinates_tuple(
                horizontal, vertical, current_field
            )
            if field.attacked_cell(
                coordinates=coordinates, field=current_field, enemy_color=enemy_color
            ):
                return False

        return True if not self.moved and not king[-1].moved else False


class Bishop(Figure):
    symbol = "♝"

    def move_cells(self, current_field: field.Field) -> list: ...

    def attack_cells(self, current_field: field.Field) -> list: ...


class Knight(Figure):
    symbol = "♞"

    def move_cells(self, current_field: field.Field) -> list: ...

    def attack_cells(self, current_field: field.Field) -> list: ...


class Queen(Figure):
    symbol = "♛"

    def move_cells(self, current_field: field.Field) -> list: ...

    def attack_cells(self, current_field: field.Field) -> list: ...


SWAP_FIGURES = dict(zip(SWAP_FIGURES_NAMES, (Bishop, Knight, Queen, Rook)))
