import math

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def get_x(self): return self._x
    def set_x(self, value: int): self._x = value
    def get_y(self): return self._y
    def set_y(self, value: int): self._y = value

    def compute_distance(self, other: 'Point') -> float:
        dx = self._x - other.get_x()
        dy = self._y - other.get_y()
        return math.sqrt(dx**2 + dy**2)


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self.compute_length()

    def get_start_point(self): return self._start_point
    def set_start_point(self, point: Point):
        self._start_point = point
        self._length = self.compute_length()

    def get_end_point(self): return self._end_point
    def set_end_point(self, point: Point):
        self._end_point = point
        self._length = self.compute_length()

    def get_length(self): return self._length

    def compute_length(self) -> float:
        return self._start_point.compute_distance(self._end_point)


class Shape:
    def __init__(self, is_regular: bool, vertices: list[Point], edges: list[Line]):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = []

    def get_is_regular(self): return self._is_regular
    def set_is_regular(self, value: bool): self._is_regular = value
    def get_vertices(self): return self._vertices
    def set_vertices(self, points: list[Point]): self._vertices = points
    def get_edges(self): return self._edges
    def set_edges(self, lines: list[Line]): self._edges = lines
    def get_inner_angles(self): return self._inner_angles
    def set_inner_angles(self, angles: list[float]): self._inner_angles = angles

    def compute_area(self): raise NotImplementedError()
    def compute_perimeter(self): return sum(edge.get_length() for edge in self._edges)
    def compute_inner_angles(self): raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, vertices: list[Point]):
        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[3]),
            Line(vertices[3], vertices[0])
        ]
        super().__init__(is_regular=False, vertices=vertices, edges=edges)

    def compute_area(self):
        width = self._edges[0].get_length()
        height = self._edges[1].get_length()
        return width * height

    def compute_inner_angles(self):
        self._inner_angles = [90.0] * 4
        return self._inner_angles

    def __str__(self):
        width = self._edges[0].get_length()
        height = self._edges[1].get_length()
        return (
            f"Rectangle:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Width: {width:.2f}, Height: {height:.2f}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )


class Square(Rectangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)

    def compute_area(self):
        side = self._edges[0].get_length()
        return side ** 2

    def __str__(self):
        side = self._edges[0].get_length()
        return (
            f"Square:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Side Length: {side:.2f}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )


class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        edges = [
            Line(vertices[0], vertices[1]),
            Line(vertices[1], vertices[2]),
            Line(vertices[2], vertices[0])
        ]
        super().__init__(is_regular=False, vertices=vertices, edges=edges)

    def compute_area(self):
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class EquilateralTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        self.set_is_regular(True)

    def compute_inner_angles(self):
        self._inner_angles = [60.0, 60.0, 60.0]
        return self._inner_angles

    def __str__(self):
        return (
            f"Equilateral Triangle:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )


class IsoscelesTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)

    def compute_inner_angles(self):
        self._inner_angles = [70.0, 70.0, 40.0]
        return self._inner_angles

    def __str__(self):
        return (
            f"Isosceles Triangle:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )


class ScaleneTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)

    def compute_inner_angles(self):
        self._inner_angles = [50.0, 60.0, 70.0]
        return self._inner_angles

    def __str__(self):
        return (
            f"Scalene Triangle:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )


class RightTriangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)

    def compute_inner_angles(self):
        self._inner_angles = [90.0, 45.0, 45.0]
        return self._inner_angles

    def __str__(self):
        return (
            f"Right Triangle:\n"
            f"- Regular: {self.get_is_regular()}\n"
            f"- Perimeter: {self.compute_perimeter():.2f}\n"
            f"- Area: {self.compute_area():.2f}\n"
            f"- Inner Angles: {self.compute_inner_angles()}°"
        )
        

if __name__ == "__main__":
    # Create points for a square with side length 2
    p1 = Point(0, 0)
    p2 = Point(0, 2)
    p3 = Point(2, 2)
    p4 = Point(2, 0)
    square = Square([p1, p2, p3, p4])

    # Create points for an equilateral triangle with side length 2
    t1 = Point(0, 0)
    t2 = Point(2, 0)
    t3 = Point(1, math.sqrt(3))  # height for equilateral triangle
    triangle = EquilateralTriangle([t1, t2, t3])

    # Print the square's information
    print(square)
    print("---------------------------------------------")

    # Print the triangle's information
    print(triangle)
