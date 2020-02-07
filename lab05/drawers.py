import cv2
import numpy as np

from lab05.models.geometry import Point, Line, Circle, Triangle


class Drawer:
    def __init__(self, canvas: np.array):
        self._canvas = canvas
        height, width, _ = self._canvas.shape
        self._z_buffer = np.full((height, width), -1.)
        self._light_vector = np.array([0, 0, -1])
        self._light_intensity = 1.2

    def draw_polygon(self, t: Triangle):
        raise NotImplementedError

    def draw_line(self, line: Line):
        raise NotImplementedError

    def draw_circle(self, c: Circle):
        raise NotImplementedError

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

    def _get_polygon_color_intensity(self, t: Triangle) -> float:
        np_p0 = t.p0.to_np_array()
        np_p1 = t.p1.to_np_array()
        np_p2 = t.p2.to_np_array()
        normal_vector: np.array = np.cross(np_p2 - np_p0, np_p1 - np_p0)
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        return self._light_vector.dot(normal_vector)

    def draw_polygon(self, t: Triangle):
        # set color intensity and skip drawing polygon if intensity <= 0
        color_intensity = self._get_polygon_color_intensity(t)
        if np.isnan(color_intensity) or color_intensity <= 0:
            return
        t.color.set_intensity(color_intensity * self._light_intensity)

        t.scale_to_screen(*self.get_dimensions())
        if t.is_height_zero():
            return
        t.sort_vertices()
        total_height: int = t.get_height()

        height, width = self.get_dimensions()
        for y in range(total_height):
            second_half: bool = y > t.p1.y - t.p0.y or t.p1.y == t.p0.y
            segment_height: int = t.p2.y - t.p1.y if second_half else t.p1.y - t.p0.y
            alpha = float(y / total_height)
            beta = float(y - (t.p1.y - t.p0.y if second_half else 0)) / segment_height

            point_a = t.p0 + (t.p2 - t.p0) * alpha
            point_b = t.p1 + (t.p2 - t.p1) * beta if second_half else t.p0 + (t.p1 - t.p0) * beta

            if point_a.x > point_b.x:
                point_a, point_b = point_b, point_a

            y_coord = int(t.p0.y + y)

            if y_coord >= height or y_coord < 0:
                continue
            # cv2.line(self._canvas,
            #          (int(point_a.x), int(point_a.y)),
            #          (int(point_b.x), int(point_b.y)),
            #          t.color.to_bgr())
            for x in range(int(point_a.x), int(point_b.x + 1)):
                if x >= width or x < 0:
                    continue
                phi: float = 1. if point_b.x == point_a.x else float(x - point_a.x) / float(point_b.x - point_a.x)
                p = Point(x, y_coord, point_a.z + (point_b.z - point_a.z) * phi)
                if self._z_buffer[y_coord, x] < p.z:
                    self._z_buffer[y_coord, x] = p.z
                    self._put_pixel(p, t.color)

    def draw_line(self, line: Line):
        steep = False
        p1 = line.start.__copy__()
        p2 = line.end.__copy__()

        if abs(p1.x - p2.x) < abs(p1.y - p2.y):
            p1.x, p1.y = p1.y, p1.x
            p2.x, p2.y = p2.y, p2.x
            steep = True

        if p1.x > p2.x:
            p1, p2 = p2, p1

        delta: Point = p2 - p1

        derror2 = abs(delta.y) * 2
        error2 = 0
        y = p1.y

        for x in range(p1.x, p2.x + 1):
            new_pixel = Point(y, x, 0) if steep else Point(x, y, 0)
            self._put_pixel(new_pixel, line.color)

            error2 += derror2
            if error2 > delta.x:
                y += 1 if p2.y > p1.y else -1
                error2 -= delta.x * 2

    def draw_circle(self, c: Circle):
        p = Point(0, c.radius, 0)

        delta = 1 - 2 * c.radius

        while p.y >= 0:
            self._put_pixel(Point(c.center.x + p.x, c.center.y + p.y, p.z), c.color)
            self._put_pixel(Point(c.center.x + p.x, c.center.y - p.y, p.z), c.color)
            self._put_pixel(Point(c.center.x - p.x, c.center.y + p.y, p.z), c.color)
            self._put_pixel(Point(c.center.x - p.x, c.center.y - p.y, p.z), c.color)

            error = 2 * (delta + p.y) - 1
            if delta < 0 and error <= 0:
                p.x += 1
                delta += 2 * p.x + 1
                continue

            error = 2 * (delta - p.x) - 1
            if delta > 0 and error > 0:
                p.y -= 1
                delta += 1 - 2 * p.y
                continue

            p.x += 1
            delta += 2 * (p.x - p.y)
            p.y -= 1
