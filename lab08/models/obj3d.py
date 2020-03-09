from typing import List, Tuple

from OpenGL.GL import *

from lab08.models.color import Color
from lab08.models.polygon import Polygon
from lab08.models.vertex import Vertex


class ObjModel:
    def __init__(self, polygons: List[Polygon] = None):
        self._polygons: List[Polygon] = polygons if polygons is not None else []
        self._rotation = (0., 0., 0.)
        self._position = (0., 0., 0.)

    @classmethod
    def from_file(cls, file_path):
        vertices: List[Vertex] = []
        faces_indexes: List[Tuple] = []
        with open(file_path, 'r') as input_file:
            for line in input_file:
                line = line.strip()
                if line.startswith("v "):
                    vertices.append(Vertex(tuple(map(float, line[2:].split(" ")))))
                elif line.startswith("f "):
                    faces_indexes.append(tuple(map(int, map(lambda x: x.split("/", 1)[0], line[2:].split(" ")))))
                else:
                    continue
        # put vertices values to corresponding faces
        polygons = [Polygon((vertices[f0 - 1], vertices[f1 - 1], vertices[f2 - 1]), Color.random())
                    for (f0, f1, f2) in faces_indexes]

        return cls(polygons)

    def draw_opengl(self):
        # save matrix before rotation and translation
        glPushMatrix()

        # translate model
        glTranslated(*self._position)

        # rotate model
        glRotatef(self._rotation[0], 1, 0, 0)
        glRotatef(self._rotation[1], 0, 1, 0)
        glRotatef(self._rotation[2], 0, 0, 1)

        # start drawing polygons
        glBegin(GL_TRIANGLES)
        for polygon in self._polygons:
            glNormal3f(*polygon.normal)
            glColor3fv(polygon.color.rgb())
            for vertex in polygon:
                glVertex3fv(vertex.tuple)
        # end drawing
        glEnd()

        # release matrix
        glPopMatrix()

    def rotate(self, x: float, y: float, z: float):
        new_x = (self._rotation[0] + x) % 360
        new_y = (self._rotation[1] + y) % 360
        new_z = (self._rotation[2] + z) % 360
        self._rotation = (new_x, new_y, new_z)

    def translate(self, x: float, y: float, z: float):
        self._position = (self._position[0] + x, self._position[1] + y, self._position[2] + z)
