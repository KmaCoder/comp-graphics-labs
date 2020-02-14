import cv2
import numpy as np

from lab06.models.light import Light
from lab06.models.line import Line
from lab06.models.obj3d import ObjModel
from lab06.models.point import Point
from lab06.models.polygon import Polygon


class Drawer:
    def __init__(self, canvas: np.array):
        self._canvas = canvas
        height, width, _ = self._canvas.shape
        self._z_buffer = np.full((height, width), -1.)
        self._light = Light(0.1, 0.8, 25, np.array([0, 0, -1]))

    def draw_polygon(self, t: Polygon, set_scaled=False):
        raise NotImplementedError

    def draw_line(self, line: Line):
        raise NotImplementedError

    def draw_model(self, model: ObjModel):
        for polygon in model.polygons:
            self.draw_polygon(polygon, model.set_scaled)

    def draw_model_skeleton(self, model: ObjModel):
        for polygon in model.polygons:
            for i in range(3):
                v0 = polygon.get_vi(i)
                v1 = polygon.get_vi((i + 1) % 3)
                self.draw_line(Line(v0, v1, polygon.color))

    def get_dimensions(self):
        height, width, _ = self._canvas.shape
        return height, width

    def flip_x(self):
        self._canvas = np.flip(self._canvas, 0)

    def show_img(self, window_name: str):
        cv2.imshow(window_name, self._canvas)

    def _put_pixel(self, p: Point, color):
        height, width = self.get_dimensions()
        x = int(p.x)
        y = int(p.y)
        if x < 0 or x > width - 1 or y < 0 or y > height - 1:
            return
        self._canvas.itemset(y, x, 0, color.b)
        self._canvas.itemset(y, x, 1, color.g)
        self._canvas.itemset(y, x, 2, color.r)


class DrawerBresenham(Drawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_polygon(self, polygon: Polygon, set_scaled=False):
        if polygon.is_height_zero():
            return

        p = polygon.get_scaled_to_screen(*self.get_dimensions()) if set_scaled else polygon
        p.sort_vertices()

        color = self._light.calc_color(polygon)
        total_height: int = p.get_height()
        height, width = self.get_dimensions()

        for y in range(total_height):
            second_half: bool = y > p.v2.y - p.v1.y or p.v2.y == p.v1.y
            segment_height: int = p.v3.y - p.v2.y if second_half else p.v2.y - p.v1.y
            alpha = float(y / total_height)
            beta = float(y - (p.v2.y - p.v1.y if second_half else 0)) / segment_height

            point_a = p.v1 + (p.v3 - p.v1) * alpha
            point_b = p.v2 + (p.v3 - p.v2) * beta if second_half else p.v1 + (p.v2 - p.v1) * beta

            if point_a.x > point_b.x:
                point_a, point_b = point_b, point_a

            y_coord = int(p.v1.y + y)

            if y_coord >= height or y_coord < 0:
                continue

            for x in range(int(point_a.x), int(point_b.x + 1)):
                if x >= width or x < 0:
                    continue
                phi: float = 1. if point_b.x == point_a.x else float(x - point_a.x) / float(point_b.x - point_a.x)
                pixel = Point.from_numbers(x, y_coord, point_a.z + (point_b.z - point_a.z) * phi)
                if self._z_buffer[y_coord, x] < pixel.z:
                    self._z_buffer[y_coord, x] = pixel.z
                    self._put_pixel(pixel, color)

    def draw_line(self, line: Line):
        steep = False
        start = line.start.get_scaled_to_screen(*self.get_dimensions())
        end = line.end.get_scaled_to_screen(*self.get_dimensions())

        if abs(start.x - end.x) < abs(start.y - end.y):
            start.x, start.y = start.y, start.x
            end.x, end.y = end.y, end.x
            steep = True

        if start.x > end.x:
            start, end = end, start

        delta: Point = end - start

        derror2 = abs(delta.y) * 2
        error2 = 0
        y = int(start.y)

        for x in range(int(start.x), int(end.x) + 1):
            new_pixel = Point.from_numbers(y, x, 0) if steep else Point.from_numbers(x, y, 0)
            self._put_pixel(new_pixel, line.color)

            error2 += derror2
            if error2 > delta.x:
                y += 1 if end.y > start.y else -1
                error2 -= delta.x * 2
