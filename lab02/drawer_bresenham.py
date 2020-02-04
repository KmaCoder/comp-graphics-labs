import cv2

from lab02.point import Point


class DrawerBresenham:
    def __init__(self, canvas):
        self._canvas = canvas

    def draw_line(self, p1: Point, p2: Point, color):
        """
        :param p1: start point
        :param p2: end point
        :param color: in BGR format
        """
        steep = False

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
            self.put_pixel(new_pixel, color)

            error2 += derror2
            if error2 > delta.x:
                y += 1 if p2.y > p1.y else -1
                error2 -= delta.x * 2

    def draw_circle(self, center: Point, r: int, color):
        p = Point(0, r)

        delta = 1 - 2 * r

        while p.y >= 0:
            self.put_pixel(Point(center.x + p.x, center.y + p.y), color)
            self.put_pixel(Point(center.x + p.x, center.y - p.y), color)
            self.put_pixel(Point(center.x - p.x, center.y + p.y), color)
            self.put_pixel(Point(center.x - p.x, center.y - p.y), color)

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

    def put_pixel(self, p: Point, color):
        shape = self._canvas.shape
        if p.x < 0 or p.x > shape[1] - 1 or p.y < 0 or p.y > shape[0] - 1:
            return
        self._canvas.itemset(p.y, p.x, 0, color[0])
        self._canvas.itemset(p.y, p.x, 1, color[1])
        self._canvas.itemset(p.y, p.x, 2, color[2])

    def show_img(self):
        cv2.imshow('image', self._canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
