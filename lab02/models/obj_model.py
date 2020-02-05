from typing import List, Tuple

from lab02.drawers import Drawer
from lab02.models.geom_models import Line, Point


class ObjModel:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self.vertices: List[Tuple] = []
        self.faces: List[Tuple] = []

        self._parse()

    def draw_model(self, drawer: Drawer, color):
        height, width = drawer.get_dimensions()
        for face in self.faces:
            for i in range(3):
                x0, y0, _ = self.vertices[face[i] - 1]
                x1, y1, _ = self.vertices[face[(i + 1) % 3] - 1]

                x0 = (x0 + 1.) * width / 2.
                y0 = (y0 + 1.) * height / 2.
                x1 = (x1 + 1.) * width / 2.
                y1 = (y1 + 1.) * height / 2.

                drawer.draw_line(Line(Point(int(x0), int(y0)), Point(int(x1), int(y1)), color))

    def _parse(self):
        with open(self._file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    self.vertices.append(tuple(map(float, line[2:].split(" "))))
                elif line.startswith("f "):
                    self.faces.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
