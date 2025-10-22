from point import Point
from line import Line
from shape import Shape

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