class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    @staticmethod
    def validate(x, y) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Координаты должны быть целыми числами.")
        if x < 0 or y < 0:
            raise ValueError("Координаты должны быть положительными числами")

    def __str__(self) -> str:
        return f"Точка с координатами: {self.x} и {self.y}"


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start: Point = start
        self.end: Point = end

    @staticmethod
    def validate(start, end) -> None:
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise ValueError("Начало и конец отрезка должны быть точками")

    def __str__(self) -> str:
        return f"Отрезок с точками ({self.start.x}, {self.start.y}) и ({self.end.x}, {self.end.y})"


class Circle:
    def __init__(self, center: Point, radius: int) -> None:
        self.center: Point = center
        self.radius: int = radius

    @staticmethod
    def validate(center, radius) -> None:
        if not isinstance(center, Point):
            raise ValueError("Центр круга должен быть точкой.")
        if not isinstance(radius, int) or radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом.")

    def __str__(self) -> str:
        return (
            f"Круг с центром в точке ({self.center.x}, "
            f"{self.center.y}) и радиусом {self.radius}"
        )


class Square:
    def __init__(self, top_left_point: Point, side_length: int) -> None:
        self.top_left_point: Point = top_left_point
        self.side_length: int = side_length

    @staticmethod
    def validate(top_left_point, side_length) -> None:
        if not isinstance(top_left_point, Point):
            raise ValueError("Верхний левый угол квадрата должен быть точкой.")
        if not isinstance(side_length, int) or side_length <= 0:
            raise ValueError("Длина стороны квадрата должна быть положительным числом.")

    def __str__(self) -> str:
        return (
            f"Квадрат с началом в точке ({self.top_left_point.x}, "
            f"{self.top_left_point.y}) и стороной {self.side_length}"
        )
