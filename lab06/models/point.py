from typing import Tuple

import numpy as np


class Point:
    def __init__(self, np_array: np.array):
        self._np_array = np_array

    @classmethod
    def from_numbers(cls, x, y, z):
        return cls(np.array((x, y, z)))

    @classmethod
    def from_tuple(cls, t: Tuple):
        return cls(np.array((t[0], t[1], t[2])))

    @property
    def x(self):
        return self._np_array[0]

    @property
    def y(self):
        return self._np_array[1]

    @property
    def z(self):
        return self._np_array[2]

    @property
    def np_array(self):
        return self._np_array

    @x.setter
    def x(self, value):
        self._np_array[0] = value

    @y.setter
    def y(self, value):
        self._np_array[1] = value

    @z.setter
    def z(self, value):
        self._np_array[2] = value

    @np_array.setter
    def np_array(self, value: np.array):
        self._np_array = value

    def __copy__(self):
        return Point(np.copy(self._np_array))

    def __add__(self, other: 'Point'):
        return Point(self._np_array + other._np_array)

    def __sub__(self, other: 'Point'):
        return Point(self._np_array - other._np_array)

    def __mul__(self, other):
        return Point(self._np_array * other)

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def get_scaled_to_screen(self, height, width) -> 'Point':
        x = int((self.x + 1.) * width / 2)
        y = abs(int(height - (self.y + 1.) * height / 2.))
        return self.from_numbers(x, y, self.z)
