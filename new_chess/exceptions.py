class FieldErrors(Exception):
    pass


class FigureColorError(FieldErrors):
    def __str__(self):
        return "Неверно указан цвет фигуры, возможно только: black или white"
