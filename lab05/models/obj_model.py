import random
from typing import List, Tuple

import numpy as np

from lab05.drawers import Drawer
from lab05.models.geom_models import Line, Point, Triangle


class ObjModel:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._vertices: List[Tuple] = []
        self._faces: List[Tuple] = []

        self._parse()

    def draw_model_skeleton(self, drawer: Drawer, color):
        height, width = drawer.get_dimensions()
        for face in self._faces:
            for i in range(3):
                x0, y0, z0 = self._vertices[face[i] - 1]
                x1, y1, z1 = self._vertices[face[(i + 1) % 3] - 1]

                p0 = Point((x0 + 1.) * width / 2., (y0 + 1.) * height / 2., z0)
                p1 = Point((x1 + 1.) * width / 2., (y1 + 1.) * height / 2., z1)

                drawer.draw_line(Line(p0, p1, color))
        drawer.flip_x()

    def draw_model_filled(self, drawer: Drawer):
        height, width = drawer.get_dimensions()

        for face in self._faces:
            screen_coords: List[Point] = []
            world_coords: List[np.array] = []
            for i in range(3):
                x, y, z = self._vertices[face[i] - 1]
                screen_coords.append(Point((x + 1.) * width / 2., abs(height - (y + 1.) * height / 2.), z))
                world_coords.append(np.array([x, y, z]))

            n: np.array = np.cross(world_coords[2] - world_coords[0], world_coords[1] - world_coords[0])
            n = n / np.linalg.norm(n)
            intensity: float = n.dot(np.array([0, 0, -1]))

            if intensity > 0:
                max_color = int(255 * intensity)
                rand_color = (random.randint(0, max_color), random.randint(0, max_color), random.randint(0, max_color))
                drawer.draw_polygon(Triangle(screen_coords[0], screen_coords[1], screen_coords[2], rand_color))

    def _parse(self):
        with open(self._file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    self._vertices.append(tuple(map(float, line[2:].split(" "))))
                elif line.startswith("f "):
                    self._faces.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
        # self._faces.sort(key=lambda x: x[2], reverse=True)
