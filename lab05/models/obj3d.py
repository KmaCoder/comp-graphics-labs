from typing import List, Tuple

import numpy as np

from lab05.drawers import Drawer
from lab05.models.geometry import Line, Point, Triangle
from lab05.models.color import Color


class ObjModel:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._faces: List[Tuple] = []
        self._parse()

    def rotate(self, theta_x, theta_y, theta_z, origin=(0, 0, 0)):
        mtrx = np.array(
            # X
            [[1, 0, 0],
             [0, np.cos(np.radians(-theta_x)), -np.sin(np.radians(-theta_x))],
             [0, np.sin(np.radians(-theta_x)), np.cos(np.radians(-theta_x))]],
        ).dot(
            # Y
            np.array([
                [np.cos(np.radians(-theta_y)), 0, np.sin(np.radians(-theta_y))],
                [0, 1, 0],
                [-np.sin(np.radians(-theta_y)), 0, np.cos(np.radians(-theta_y))]
            ])
        ).dot(
            # Z
            np.array([
                [np.cos(np.radians(-theta_z)), -np.sin(np.radians(-theta_z)), 0],
                [np.sin(np.radians(-theta_z)), np.cos(np.radians(-theta_z)), 0],
                [0, 0, 1]
            ])
        )
        self._faces = [
            tuple(
                mtrx.dot(
                    np.transpose(v - np.array(origin))
                ) + np.array(origin)
                for v in vs
            )
            for vs
            in self._faces
        ]

    def draw_model_skeleton(self, drawer: Drawer):
        height, width = drawer.get_dimensions()
        # color = Color.random()
        color = Color(150, 255, 100)
        for face in self._faces:
            for i in range(3):
                x0, y0, z0 = face[i]
                x1, y1, z1 = face[(i + 1) % 3]

                p0 = Point(x0, y0, z0).scale_to_screen(height, width)
                p1 = Point(x1, y1, z1).scale_to_screen(height, width)

                drawer.draw_line(Line(p0, p1, color))

    def draw_model(self, drawer: Drawer):
        for face in self._faces:
            color = Color(255, 213, 150)
            # color = Color.random()
            coords: List[Point] = []
            for i in range(3):
                x, y, z = face[i]
                coords.append(Point(x, y, z))
            drawer.draw_polygon(Triangle(coords[0], coords[1], coords[2], color))

    def _parse(self):
        vertices: List[np.array] = []
        faces_indexes: List[Tuple] = []
        with open(self._file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    vertices.append(np.array(tuple(map(float, line[2:].split(" ")))))
                elif line.startswith("f "):
                    faces_indexes.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
        # put vertices values to corresponding faces
        self._faces = [(vertices[f0 - 1], vertices[f1 - 1], vertices[f2 - 1]) for (f0, f1, f2) in faces_indexes]
