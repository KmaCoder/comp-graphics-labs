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
        k: float = (p2.y - p1.y) / (p2.x - p1.y)
        d: float = 2 * k - 1
        y = p1.y
        self.put_pixel(p1, color)

        for x in range(p1.x, p2.x):
            if d > 0:
                d += 2 * k - 2
                y += 1
            else:
                d += 2 * k
            self.put_pixel(Point(x, y), color)

    def put_pixel(self, p: Point, color):
        self._canvas.itemset(p.y, p.x, 0, color[0])
        self._canvas.itemset(p.y, p.x, 1, color[1])
        self._canvas.itemset(p.y, p.x, 2, color[2])

    def show_img(self):
        cv2.imshow('image', self._canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
