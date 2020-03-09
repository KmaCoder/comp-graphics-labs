from math import cos, sin, pi
from typing import List

import numpy as np

from lab08.models.color import Color
from lab08.models.obj3d import ObjModel
from lab08.models.vertex import Vertex
from lab08.models.polygon import Polygon


def rotate(vertex, theta_x=0., theta_y=0., theta_z=0.):
    arr: np.ndarray = np.array(
        # X
        [[1, 0, 0],
         [0, cos(-theta_x), -sin(-theta_x)],
         [0, sin(-theta_x), cos(-theta_x)]],
    ).dot(
        # Y
        np.array([
            [cos(-theta_y), 0, sin(-theta_y)],
            [0, 1, 0],
            [-sin(-theta_y), 0, cos(-theta_y)]
        ])
    ).dot(
        # Z
        np.array([
            [cos(-theta_z), -sin(-theta_z), 0],
            [sin(-theta_z), cos(-theta_z), 0],
            [0, 0, 1]
        ])
    ).dot(
        np.transpose(np.array(vertex))
    )
    return arr.tolist()


def translate(vertex, vector):
    return np.array(vertex) + np.array(vector)


def circle(r, vertices_count):
    for i in range(vertices_count):
        angle = 2 * pi * i / vertices_count
        yield (r * cos(angle)), (r * sin(angle)), 0


def move_cycle(arr: list):
    copy = arr[1:]
    return copy + [arr[0]]


class Torus(ObjModel):
    def __init__(self, R: float, r: float, vertices_count: int):
        cut_circles = []
        for i in range(vertices_count):
            angle = 2 * pi * i / vertices_count
            translate_vector = [R * cos(angle), 0, R * sin(angle)]
            cut_circles.append(
                [
                    translate(rotate(vertex, theta_y=angle), translate_vector)
                    for vertex
                    in circle(r, vertices_count)
                ]
            )
        faces: List[Polygon] = []
        for circle1, circle2 in zip(cut_circles, move_cycle(cut_circles)):
            for v1, v2, v3, v4 in zip(circle1, move_cycle(circle1), circle2, move_cycle(circle2)):
                faces.extend([
                    Polygon((Vertex(v1), Vertex(v2), Vertex(v3)), Color.random()),
                    Polygon((Vertex(v2), Vertex(v4), Vertex(v3)), Color.random())
                ])
        super().__init__(faces)
