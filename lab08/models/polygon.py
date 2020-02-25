from typing import Tuple, List

import numpy as np

from lab08.models.color import Color
from lab08.models.vertex import Vertex


class Polygon:
    def __init__(self, vertices: Tuple[Vertex, ...], color: Color):
        self._vertices = vertices
        self._color: Color = color
        self._normal: List = []
        self._calc_normal()

    def get_vertex(self, i) -> Vertex:
        return self._vertices[i]

    def _calc_normal(self):
        x1, y1, z1 = self.get_vertex(0).tuple
        x2, y2, z2 = self.get_vertex(1).tuple
        x3, y3, z3 = self.get_vertex(2).tuple
        normal_vector: np.ndarray = np.array([
            (y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1),
            (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1),
            (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        ])
        self._normal = normal_vector.tolist()

    @property
    def polygon(self) -> Tuple[Vertex, ...]:
        return self._vertices

    @property
    def normal(self) -> List:
        return self._normal

    @property
    def color(self) -> Color:
        return self._color
