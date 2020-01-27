import cv2
import numpy as np

from lab02.point import Point


class DrawerBresenham:
    def __init__(self, canvas_width: int, canvas_height: int):
        self.__canvas = np.zeros((canvas_width, canvas_height, 3), np.uint8)

    def draw_line(self, p1: Point, p2: Point, color):
        """
        :param p1: start point
        :param p2: end point
        :param color: in BGR format
        """
        k: float = (p2.y - p1.y) / (p2.x - p1.y)
        d: float = 2 * k - 1
        y = p1.y
        self.__put_pixel(p1, color)

        for x in range(p1.x, p2.x):
            if d > 0:
                d += 2 * k - 2
                y += 1
            else:
                d += 2 * k
            self.__put_pixel(Point(x, y), color)

    def __put_pixel(self, p: Point, color):
        self.__canvas.itemset(p.y, p.x, 0, color[0])
        self.__canvas.itemset(p.y, p.x, 1, color[1])
        self.__canvas.itemset(p.y, p.x, 2, color[2])

    def show_img(self):
        cv2.imshow('image', self.__canvas)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
