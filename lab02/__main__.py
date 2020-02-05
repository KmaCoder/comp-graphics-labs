import numpy as np
from typing import List

from lab02.drawers import DrawerBresenham, DrawerCV2, Drawer
from lab02.models.geom_models import Point, Line, Circle
from lab02.models.obj_model import ObjModel
from lab02.utils import wait_space_click


def lines_and_circles():
    def draw_lines_and_circles(lines: List[Line], circles: List[Circle], drawer: Drawer, window_name: str):
        for l in lines:
            drawer.draw_line(l)
        for c in circles:
            drawer.draw_circle(c)
        drawer.show_img(window_name)

    height, width = 600, 600
    lines_task1 = [
        # table lines
        Line(Point(200, 0), Point(200, 600), (200, 100, 100)),
        Line(Point(400, 0), Point(400, 600), (200, 100, 100)),
        Line(Point(0, 200), Point(600, 200), (200, 100, 100)),
        Line(Point(0, 400), Point(600, 400), (200, 100, 100)),
        # crosses
        Line(Point(0, 0), Point(200, 200), (100, 100, 200)),
        Line(Point(0, 200), Point(200, 0), (100, 100, 200)),
        Line(Point(200, 200), Point(400, 400), (100, 100, 200)),
        Line(Point(200, 400), Point(400, 200), (100, 100, 200)),
        Line(Point(400, 400), Point(600, 600), (100, 100, 200)),
        Line(Point(400, 600), Point(600, 400), (100, 100, 200)),
    ]
    circles_task1 = [
        Circle(Point(100, 500), 99, (100, 200, 100)),
        Circle(Point(300, 100), 99, (100, 200, 100)),
        Circle(Point(500, 300), 99, (100, 200, 100)),
    ]

    lines_canvas_cv2 = np.zeros((height, width, 3), np.uint8)
    draw_lines_and_circles(lines_task1,
                           circles_task1,
                           DrawerCV2(lines_canvas_cv2),
                           "Lines and circles with cv2")

    lines_canvas = np.zeros((height, width, 3), np.uint8)
    draw_lines_and_circles(lines_task1,
                           circles_task1,
                           DrawerBresenham(lines_canvas),
                           "Lines and circles Bresenham")


def head_model():
    height, width = 600, 600
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/lab02/materials/african_head.obj")

    model_canvas = np.zeros((height, width, 3), np.uint8)
    model_drawer = DrawerBresenham(model_canvas)
    obj_model.draw_model(model_drawer, (100, 255, 100))
    model_drawer.show_img("Head model using DrawerBresenham")

    model_canvas_cv2 = np.zeros((height, width, 3), np.uint8)
    model_drawer_cv2 = DrawerCV2(model_canvas_cv2)
    obj_model.draw_model(model_drawer_cv2, (100, 100, 255))
    model_drawer_cv2.show_img("Head model using DrawerCV2")


if __name__ == "__main__":
    lines_and_circles()
    head_model()
    wait_space_click()
