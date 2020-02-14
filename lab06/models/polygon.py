from typing import Tuple

from lab06.models.color import Color
from lab06.models.point import Point


class Polygon:
    def __init__(self, v1: Point, v2: Point, v3: Point, color: Color):
        self._vertices = [v1, v2, v3]
        self.color = color

    def __iter__(self):
        return iter(self._vertices)

    # def __copy__(self):
    #     return Polygon.from_tuple(
    #         tuple(map(lambda x: x.__copy__(), self._vertices)),
    #         self.color.__copy__()
    #     )

    @classmethod
    def from_tuple(cls, t: Tuple, color: Color):
        return cls(t[0], t[1], t[2], color)

    @property
    def v1(self):
        return self._vertices[0]

    @property
    def v2(self):
        return self._vertices[1]

    @property
    def v3(self):
        return self._vertices[2]

    def get_vi(self, i):
        return self._vertices[i]

    def sort_vertices(self):
        self._vertices.sort(key=lambda x: x.y)

    def is_height_zero(self):
        return self.v1.y == self.v2.y and self.v1.y == self.v3.y

    def get_height(self) -> int:
        """
        Vertices must be sorted before calling this function
        :return: height
        """
        return int(self.v3.y - self.v1.y)

    def get_scaled_to_screen(self, height, width) -> 'Polygon':
        return Polygon.from_tuple(
            tuple(map(lambda x: x.get_scaled_to_screen(height, width), self._vertices)),
            self.color.__copy__()
        )
