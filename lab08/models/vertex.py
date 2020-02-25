from typing import Tuple


class Vertex:
    def __init__(self, vertex: Tuple[float, float, float]):
        self._tuple = vertex

    @property
    def x(self) -> float:
        return self._tuple[0]

    @property
    def y(self) -> float:
        return self._tuple[1]

    @property
    def z(self) -> float:
        return self._tuple[2]

    @property
    def tuple(self) -> Tuple[float, float, float]:
        return self._tuple
