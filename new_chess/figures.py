from abc import ABC, abstractmethod
from settings import FIGURE_COLOR
import exceptions
import field


class Figure(ABC):
    def __init__(self, x_coordinate: int, y_coordinate: int, color: str):
        if color not in FIGURE_COLOR:
            raise exceptions.FigureColorError

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color

    @abstractmethod
    def move_cells(self, field: field.Field) -> list: ...


class Soldier(Figure):
    symbol = "♟"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moved = False

    # def move_cells(self, field: field.Field):
    #     return super().move_cells(field)

    def move_cells(self, field: field.Field) -> list:
        result = []

        start = (
            self.x_coordinate if self.x_coordinate - 1 < 0 else self.x_coordinate - 1
        )
        end = self.x_coordinate if self.x_coordinate + 1 > 7 else self.x_coordinate + 1
        vertical = self.get_vertical()  # exceptions.EndOfField
        braker = False

        for horizontal, cell in enumerate(
            field[vertical][start : end + 1], start=start
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
            and field[self.get_vertical(action=1)][self.x_coordinate - 1][-1] is None
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


class King(Figure):
    symbol = "♚"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.moved = False

    def move_cells(self, field: field.Field) -> list:
        result = []
