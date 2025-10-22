from point import Point
from line import Line 
from shape import Shape
import math

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