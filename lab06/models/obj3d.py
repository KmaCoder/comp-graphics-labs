from typing import List

import numpy as np

from lab06.models.color import Color
from lab06.models.point import Point
from lab06.models.polygon import Polygon


class ObjModel:
    def __init__(self, file_path: str = None, set_scaled: bool = False):
        self._position = np.array((0, 0, 0))
        self.set_scaled = set_scaled
        self.polygons: List[Polygon] = []
        if file_path:
            self._parse(file_path)

    def rotate(self, theta_x, theta_y, theta_z):
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

        self.polygons = [
            Polygon.from_tuple(
                tuple(
                    Point(mtrx.dot(
                        np.transpose(v.np_array - self._position)
                    ) + self._position)
                    for v in polygon
                ),
                polygon.color
            )
            for polygon in self.polygons
        ]

    def translate(self, v: np.array):
        self._position += v
        for polygon in self.polygons:
            for vertix in polygon:
                vertix.np_array += v

    def _parse(self, file_path):
        vertices: List[Point] = []
        faces_indexes = []
        with open(file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    vertices.append(Point(np.array(tuple(map(float, line[2:].split(" "))))))
                elif line.startswith("f "):
                    faces_indexes.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
        # put vertices values to corresponding faces
        # Color(255, 213, 150)
        self.polygons = [Polygon(vertices[f0 - 1], vertices[f1 - 1], vertices[f2 - 1], Color.random())
                         for (f0, f1, f2) in faces_indexes]
