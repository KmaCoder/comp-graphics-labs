import cv2
import numpy as np

from lab03.models.geom_models import Point, Line, Circle
from lab03.models.geom_models import Triangle


class Drawer:
    def __init__(self, canvas: np.array):
        self._canvas = canvas

    def draw_line(self, line: Line):
        raise NotImplementedError

    def draw_circle(self, c: Circle):
        raise NotImplementedError

    def draw_filled_triangle(self, t: Triangle):
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
        if p.x < 0 or p.x > width - 1 or p.y < 0 or p.y > height - 1:
            return
        self._canvas.itemset(p.y, p.x, 0, color[0])
        self._canvas.itemset(p.y, p.x, 1, color[1])
        self._canvas.itemset(p.y, p.x, 2, color[2])


class DrawerBresenham(Drawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_line(self, line: Line):
        steep = False
        p1 = line.start.__copy__()
        p2 = line.end.__copy__()

        if abs(p1.x - p2.x) < abs(p1.y - p2.y):
            p1.swap_xy()
            p2.swap_xy()
            steep = True

        if p1.x > p2.x:
            p1, p2 = p2, p1

        delta: Point = p2 - p1

        derror2 = abs(delta.y) * 2
        error2 = 0
        y = p1.y

        for x in range(p1.x, p2.x + 1):
            new_pixel = Point(y, x) if steep else Point(x, y)
            self._put_pixel(new_pixel, line.color)

            error2 += derror2
            if error2 > delta.x:
                y += 1 if p2.y > p1.y else -1
                error2 -= delta.x * 2

    def draw_circle(self, c: Circle):
        p = Point(0, c.radius)

        delta = 1 - 2 * c.radius

        while p.y >= 0:
            self._put_pixel(Point(c.center.x + p.x, c.center.y + p.y), c.color)
            self._put_pixel(Point(c.center.x + p.x, c.center.y - p.y), c.color)
            self._put_pixel(Point(c.center.x - p.x, c.center.y + p.y), c.color)
            self._put_pixel(Point(c.center.x - p.x, c.center.y - p.y), c.color)

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

    def draw_filled_triangle(self, t: Triangle):
        if t.is_height_zero():
            return
        t.sort_vertices()
        total_height: int = t.get_height()
        for y in range(total_height):
            second_half: bool = y > t.p1.y - t.p0.y or t.p1.y == t.p0.y
            segment_height: int = t.p2.y - t.p1.y if second_half else t.p1.y - t.p0.y
            alpha: float = y / total_height
            # be careful: with above conditions no division by zero here
            beta: float = (y - (t.p1.y - t.p0.y if second_half else 0)) / segment_height

            point1 = t.p0 + (t.p2 - t.p0) * alpha
            point2 = t.p1 + (t.p2 - t.p1) * beta if second_half else t.p0 + (t.p1 - t.p0) * beta

            if point1.x > point2.x:
                point1, point2 = point2, point1

            for x in range(point1.x, point2.x + 1):
                self._put_pixel(Point(x, t.p0.y + y), t.color)


class DrawerCV2(Drawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_line(self, line: Line):
        cv2.line(self._canvas, (line.start.x, line.start.y), (line.end.x, line.end.y), line.color)

    def draw_circle(self, c: Circle):
        cv2.circle(self._canvas, (c.center.x, c.center.y), c.radius, c.color)

    def draw_filled_triangle(self, t: Triangle):
        cv2.drawContours(self._canvas, [
            np.array([(int(t.p0.x), int(t.p0.y)), (int(t.p1.x), int(t.p1.y)), (int(t.p2.x), int(t.p2.y))])], 0,
                         t.color, -1)
