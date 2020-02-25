from typing import List, Tuple

from OpenGL.GL import *

from lab08.models.color import Color
from lab08.models.polygon import Polygon
from lab08.models.vertex import Vertex


class ObjModel:
    def __init__(self, polygons=None):
        self.polygons: List[Polygon] = polygons if polygons is not None else []
        # self._position = np.array((0, 0, 0))

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
        glBegin(GL_TRIANGLES)
        for polygon in self.polygons:
            glColor3fv(polygon.color.rgb())
            glVertex3fv(polygon.get_vertex(0).tuple)
            glVertex3fv(polygon.get_vertex(1).tuple)
            glVertex3fv(polygon.get_vertex(2).tuple)
        glEnd()
