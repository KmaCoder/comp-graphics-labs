import random
from typing import Tuple


class Color:
    def __init__(self, r: float = 0, g: float = 0, b: float = 0):
        self._tuple: Tuple[float, float, float] = (r, g, b)

    def __copy__(self):
        return Color(self.r, self.g, self.b)

    @classmethod
    def random(cls) -> 'Color':
        return cls(random.random(), random.random(), random.random())

    @property
    def r(self) -> float:
        return self._tuple[0]

    @property
    def g(self) -> float:
        return self._tuple[1]

    @property
    def b(self) -> float:
        return self._tuple[2]

    def rgb(self) -> Tuple[float, float, float]:
        return self._tuple

    def set_intensity(self, intensity: float):
        self._tuple = (min(self.r * intensity, 1), min(self.g * intensity, 1), min(self.b * intensity, 1))
