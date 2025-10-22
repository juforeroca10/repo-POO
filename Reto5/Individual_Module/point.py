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