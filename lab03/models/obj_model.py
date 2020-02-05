import random
from typing import List, Tuple

from lab03.drawers import Drawer
from lab03.models.geom_models import Line, Point, Triangle


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
                x0, y0, _ = self._vertices[face[i] - 1]
                x1, y1, _ = self._vertices[face[(i + 1) % 3] - 1]

                p0 = Point((x0 + 1.) * width / 2., (y0 + 1.) * height / 2.)
                p1 = Point((x1 + 1.) * width / 2., (y1 + 1.) * height / 2.)

                drawer.draw_line(Line(p0, p1, color))
        drawer.flip_x()

    def draw_model_filled(self, drawer: Drawer):
        height, width = drawer.get_dimensions()
        for face in self._faces:
            for i in range(3):
                x0, y0, _ = self._vertices[face[0] - 1]
                x1, y1, _ = self._vertices[face[1] - 1]
                x2, y2, _ = self._vertices[face[2] - 1]

                p0 = Point((x0 + 1.) * width / 2., abs(height - (y0 + 1.) * height / 2.))
                p1 = Point((x1 + 1.) * width / 2., abs(height - (y1 + 1.) * height / 2.))
                p2 = Point((x2 + 1.) * width / 2., abs(height - (y2 + 1.) * height / 2.))

                rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                drawer.draw_filled_triangle(Triangle(p0, p1, p2, rand_color))

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
