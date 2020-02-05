import cv2
import numpy as np

from lab02.models.geom_models import Point, Line, Circle


class Drawer:
    def __init__(self, canvas: np.array):
        self._canvas = canvas

    def draw_line(self, line: Line):
        raise NotImplementedError

    def draw_circle(self, c: Circle):
        raise NotImplementedError

    def get_dimensions(self):
        height, width, _ = self._canvas.shape
        return height, width

    def show_img(self, window_name: str):
        cv2.imshow(window_name, self._canvas)


class DrawerBresenham(Drawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_line(self, line: Line):
        steep = False
        p1 = line.start
        p2 = line.end

        if abs(p1.x - p2.x) < abs(p1.y - p2.y):
            p1.swap_xy()
            p2.swap_xy()
            steep = True

        if p1.x > p2.x:
            p1.swap_with_point(p2)

        delta = Point(p2.x - p1.x, p2.y - p1.y)

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

    def _put_pixel(self, p: Point, color):
        height, width = self.get_dimensions()
        if p.x < 0 or p.x > width - 1 or p.y < 0 or p.y > height - 1:
            return
        self._canvas.itemset(p.y, p.x, 0, color[0])
        self._canvas.itemset(p.y, p.x, 1, color[1])
        self._canvas.itemset(p.y, p.x, 2, color[2])


class DrawerCV2(Drawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw_line(self, line: Line):
        cv2.line(self._canvas, (line.start.x, line.start.y), (line.end.x, line.end.y), line.color)

    def draw_circle(self, c: Circle):
        cv2.circle(self._canvas, (c.center.x, c.center.y), c.radius, c.color)
