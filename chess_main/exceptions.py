from chess_main.settings import BACKS, END


class ChessException(Exception):
    def print_error(self):
        print(BACKS["red"] + self.__str__() + END)


class FieldErrors(ChessException):
    pass


class BackColorError(FieldErrors):
    def __str__(self):
        return "Неверно указан цвет клетки, возможно только: black, white, green, red, blue"


class FigureSymbolError(FieldErrors):
    def __str__(self):
        return "Неверно указан символ фигуры"


class FigureErrors(ChessException):
    pass


class NotFigureError(FigureErrors):
    def __str__(self):
        return "Вместо фигуры получили None"


class FigureColorError(FigureErrors):
    def __str__(self):
        return "Неверно указан цвет фигуры, возможно только: black или white"


class EndOfField(FigureErrors):
    pass


class InputError(ChessException):
    pass


class EndOfGame(ChessException):
    def __str__(self):
        return "Конец игры"


class MovesErrors(ChessException):
    pass


class ChooseFigureError(MovesErrors):
    pass


class ColorError(ChessException):
    def __str__(self):
        return "Был неверно указан цвет"


class CheckmateError(MovesErrors):
    def __str__(self):
        return "Невозможно сходить данной фигурой - это приведет к мату"
