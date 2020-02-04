import numpy as np

from lab02.drawer_bresenham import DrawerBresenham
from lab02.point import Point


canvas = np.zeros((500, 500, 3), np.uint8)
drawer = DrawerBresenham(canvas)
drawer.draw_line(Point(0, 0), Point(100, 100), (200, 100, 100))
drawer.draw_line(Point(100, 100), Point(200, 200), (100, 200, 100))
drawer.draw_line(Point(200, 200), Point(300, 300), (100, 100, 200))
drawer.show_img()
