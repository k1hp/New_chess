class FieldErrors(Exception):
    pass


class BackColorError(FieldErrors):
    def __str__(self):
        return "Неверно указан цвет клетки, возможно только: black, white, green, red"


class FigureSymbolError(FieldErrors):
    def __str__(self):
        return "Неверно указан символ фигуры"


class FigureErrors(Exception):
    pass


class NotFigureError(FigureErrors):
    def __str__(self):
        return "Вместо фигуры получили None"


class FigureColorError(FigureErrors):
    def __str__(self):
        return "Неверно указан цвет фигуры, возможно только: black или white"


class EndOfField(FigureErrors):
    pass


class InputError(Exception):
    pass


class EndOfGame(Exception):
    def __str__(self):
        return "Конец игры"


class MovesErrors(Exception):
    pass


class ChooseFigureError(MovesErrors):
    pass


class ColorError(Exception):
    def __str__(self):
        return "Был неверно указан цвет"


class CheckmateError(MovesErrors):
    def __str__(self):
        return "Невозможно сходить данной фигурой - это приведет к мату"
