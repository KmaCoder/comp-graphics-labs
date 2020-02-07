from time import time

import cv2
import numpy as np

from lab05.drawers import DrawerBresenham
from lab05.models.obj3d import ObjModel
from lab05.utils import wait_space_click


def head_model():
    height, width = 800, 800
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    model_canvas = np.zeros((height, width, 3), np.uint8)
    model_drawer = DrawerBresenham(model_canvas)
    obj_model.draw_model(model_drawer)
    model_drawer.show_img("Head filled")


def head_model_rotating():
    height, width = 600, 600
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")

    frames = []
    frames_len = 36
    for i in range(frames_len):
        print(f'\rRendering frame: {i + 1}/{frames_len}', end='')
        obj_model.rotate(10, 0, 0)
        canvas = np.zeros((height, width, 3), np.uint8)
        drawer = DrawerBresenham(canvas)
        obj_model.draw_model(drawer)
        frames.append(canvas)

    while True:
        for frame in frames:
            start = int(time() * 1000)
            cv2.imshow('model', frame)
            end = int(time() * 1000)
            cv2.waitKey(max(1, 10 - (start - end)))


if __name__ == "__main__":
    head_model_rotating()
    wait_space_click()
