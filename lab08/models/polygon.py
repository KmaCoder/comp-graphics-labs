from typing import Tuple

from lab08.models.color import Color
from lab08.models.vertex import Vertex


class Polygon:
    def __init__(self, vertices: Tuple[Vertex, ...], color: Color):
        self._vertices = vertices
        self._color = color

    def get_vertex(self, i) -> Vertex:
        return self._vertices[i]

    @property
    def polygon(self) -> Tuple[Vertex, ...]:
        return self._vertices

    @property
    def color(self) -> Color:
        return self._color
