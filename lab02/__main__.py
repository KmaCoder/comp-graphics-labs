import cv2
import numpy as np

from lab02.drawer_bresenham import DrawerBresenham
from lab02.models import Point


def lines_and_circles():
    canvas1 = np.zeros((600, 600, 3), np.uint8)

    drawer = DrawerBresenham(canvas1)
    drawer.draw_line(Point(200, 0), Point(200, 600), (200, 100, 100))
    drawer.draw_line(Point(400, 0), Point(400, 600), (200, 100, 100))
    drawer.draw_line(Point(0, 200), Point(600, 200), (200, 100, 100))
    drawer.draw_line(Point(0, 400), Point(600, 400), (200, 100, 100))

    drawer.draw_line(Point(0, 0), Point(200, 200), (100, 100, 200))
    drawer.draw_line(Point(0, 200), Point(200, 0), (100, 100, 200))

    drawer.draw_line(Point(200, 200), Point(400, 400), (100, 100, 200))
    drawer.draw_line(Point(200, 400), Point(400, 200), (100, 100, 200))

    drawer.draw_line(Point(400, 400), Point(600, 600), (100, 100, 200))
    drawer.draw_line(Point(400, 600), Point(600, 400), (100, 100, 200))

    drawer.draw_circle(Point(100, 500), 99, (100, 200, 100))
    drawer.draw_circle(Point(300, 100), 99, (100, 200, 100))
    drawer.draw_circle(Point(500, 300), 99, (100, 200, 100))

    cv2.imshow("Lines and circles", canvas1)

    while True:
        k = cv2.waitKey(33)
        if k == 32:
            break


if __name__ == "__main__":
    lines_and_circles()
