import numpy as np

from lab06.models.color import Color
from lab06.models.polygon import Polygon


class Light:
    def __init__(self, ambient_coef: float, diffuse_coef: float, specular_coef: float, light_direction: np.array):
        self._ambient_coef = ambient_coef
        self._diffuse_coef = diffuse_coef
        self._specular_coef = specular_coef
        self._light_direction = light_direction
        self._view_dir = np.array((0., 0., -1.))

    def calc_color_intensity(self, p: Polygon) -> float:
        normal_vector: np.array = np.cross((p.v3 - p.v1).np_array, (p.v2 - p.v1).np_array)
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        diffuse_light = max(self._light_direction.dot(normal_vector), 0)
        reflect_dir = 2 * normal_vector * (
                normal_vector.dot(self._light_direction) / normal_vector.dot(normal_vector)) - self._light_direction
        specular_light = pow(max(self._view_dir.dot(reflect_dir), 0.0), 32)
        return self._ambient_coef + self._diffuse_coef * diffuse_light + self._specular_coef * specular_light

    def calc_color(self, p: Polygon) -> Color:
        new_color = p.color.__copy__()
        new_color.set_intensity(self.calc_color_intensity(p))
        return new_color
