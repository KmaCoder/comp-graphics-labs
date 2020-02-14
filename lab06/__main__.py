from time import time

import cv2
import numpy as np

from lab06.drawers import DrawerBresenham
from lab06.models.obj3d import ObjModel
from lab06.models.torus import Torus
from lab06.utils import wait_space_click


def tor_model():
    height, width = 600, 600
    obj_model = Torus(R=250, r=60, vertices_count=20)
    model_canvas = np.zeros((height, width, 3), np.uint8)
    drawer = DrawerBresenham(model_canvas)
    drawer.draw_model(obj_model)
    drawer.show_img("Head filled")


def head_model():
    height, width = 600, 600
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    obj_model.rotate(0, 5, 0)
    model_canvas = np.zeros((height, width, 3), np.uint8)
    drawer = DrawerBresenham(model_canvas)
    drawer.draw_model(obj_model)
    drawer.show_img("Head filled")


def head_model_rotating():
    height, width = 600, 600
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")

    frames = []
    frames_len = 10
    for i in range(frames_len):
        print(f'\rRendering frame: {i + 1}/{frames_len}', end='')
        obj_model.rotate(0, 1, 0)
        canvas = np.zeros((height, width, 3), np.uint8)
        drawer = DrawerBresenham(canvas)
        drawer.draw_model(obj_model)
        frames.append(canvas)

    while True:
        for frame in frames:
            start = int(time() * 1000)
            cv2.imshow('model', frame)
            end = int(time() * 1000)
            cv2.waitKey(max(1, 10 - (start - end)))


if __name__ == "__main__":
    head_model()
    # head_model_rotating()
    wait_space_click()
