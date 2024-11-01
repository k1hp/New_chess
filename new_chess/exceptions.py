class FieldErrors(Exception):
    pass


class FigureErrors(Exception):
    pass


class BackColorError(FieldErrors):
    def __str__(self):
        return "Неверно указан цвет клетки, возможно только: black, white, green, red"


class FigureColorError(FigureErrors):
    def __str__(self):
        return "Неверно указан цвет фигуры, возможно только: black или white"


class FigureSymbolError(FieldErrors):
    def __str__(self):
        return "Неверно указан символ фигуры"


class EndOfField(FigureErrors):
    pass


class MovesErrors(Exception):
    pass


class ChooseFigureError(MovesErrors):
    pass


class InputError(Exception):
    pass
