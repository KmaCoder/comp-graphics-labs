import random
from typing import Tuple


class Color:
    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = r
        self.g = g
        self.b = b

    def __mul__(self, intensity: float):
        return Color(int(self.r * intensity), int(self.g * intensity), int(self.b * intensity))

    @classmethod
    def random(cls) -> 'Color':
        return cls(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def to_rgb(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    def to_bgr(self) -> Tuple[int, int, int]:
        return self.b, self.g, self.r

    def set_intensity(self, intensity: float):
        self.r = min(int(self.r * intensity), 255)
        self.g = min(int(self.g * intensity), 255)
        self.b = min(int(self.b * intensity), 255)
