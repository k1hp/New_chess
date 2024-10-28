from abc import ABC, abstractmethod
from settings import FIGURE_COLOR
import exceptions


class Figure(ABC):
    def __init__(self, x_coordinate: int, y_coordinate: int, color: str):
        if color not in FIGURE_COLOR:
            raise exceptions.FigureColorError

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.color = color

    @abstractmethod
    def can_move(self): ...


class Soldier(Figure):
    symbol = "♟"
