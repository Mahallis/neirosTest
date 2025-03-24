from shapes import Circle, Line, Point, Square


class ShapeManager:
    def __init__(self) -> None:
        self.shapes: list = []
        self.shape_options: dict = {
            "point": self.create_point,
            "line": self.create_line,
            "circle": self.create_circle,
            "square": self.create_square,
        }

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        print(f"Добавлено: {shape}")

    def remove_shape(self, index: int) -> None:
        if 0 <= index < len(self.shapes):
            removed_shape = self.shapes.pop(index)
            print(f"Удалено: {removed_shape}")
        else:
            print("Неверный индекс")

    def list_shapes(self) -> None:
        if not self.shapes:
            print("Вы еще не добавили фигуры.")
        else:
            for index, shape in enumerate(self.shapes):
                print(f"{index}: {shape}")

    def handle_shape(self, command: list) -> None:
        shape_type: str = command[1]
        measurements: list[str] = command[2:]
        is_digits: list = map(lambda x: x.isdigit(), measurements)

        allowed_shape = self.shape_options.get(shape_type)

        try:
            if not allowed_shape:
                raise ValueError("Неверный тип фигуры.")
            if not any(is_digits):
                raise ValueError("Неверные параметры измерений фигуры.")
            shape = allowed_shape([*map(int, measurements)])
            self.add_shape(shape)
        except ValueError as e:
            print(f"Ошибка при создании фигуры: {e}")

    def create_point(self, measurements: list) -> Point:
        if len(measurements) != 2:
            raise ValueError("Точка должна состоять из двух параметров.")
        x, y = measurements
        Point.validate(x, y)
        return Point(x=x, y=y)

    def create_line(self, measurements: list) -> Line:
        if len(measurements) != 4:
            raise ValueError("Отрезок должен состоять из четырех параметров.")

        start_x, start_y, end_x, end_y = measurements
        start = self.create_point((start_x, start_y))
        end = self.create_point((end_x, end_y))
        Line.validate(start, end)
        return Line(start=start, end=end)

    def create_circle(self, measurements: list) -> Circle:
        if len(measurements) != 3:
            raise ValueError("Круг должен состоять из трех параметров.")
        center_x, center_y, radius = measurements
        center = self.create_point((center_x, center_y))
        Circle.validate(center, radius)
        return Circle(center=center, radius=radius)

    def create_square(self, measurements: list) -> Square:
        if len(measurements) != 3:
            raise ValueError("Квадрат должен состоять из трех параметров.")
        top_left_x, top_left_y, side_length = measurements
        top_left_point = self.create_point((top_left_x, top_left_y))
        return Square(top_left_point=top_left_point, side_length=side_length)
