from line import Line
from point import Point

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