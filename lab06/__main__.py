from time import time

import cv2
import numpy as np

from lab06.drawers import DrawerBresenham
from lab06.models.obj3d import ObjModel
from lab06.models.torus import Torus
from lab06.utils import wait_space_click


def tor_model():
    height, width = 600, 600
    model = Torus(R=250, r=60, vertices_count=20)
    canvas = np.zeros((height, width, 3), np.uint8)
    drawer = DrawerBresenham(canvas)
    drawer.draw_model(model)
    drawer.show_img("Tor")


def head_model():
    height, width = 600, 600
    model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    model.rotate(0, 5, 0)
    canvas = np.zeros((height, width, 3), np.uint8)
    drawer = DrawerBresenham(canvas)
    drawer.draw_model(model)
    drawer.show_img("Head filled")


def head_model_rotating():
    height, width = 600, 600
    model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")

    frames = []
    frames_len = 18
    for i in range(frames_len):
        print(f'\rRendering frame: {i + 1}/{frames_len}', end='')
        model.rotate(0, 10, 0)
        canvas = np.zeros((height, width, 3), np.uint8)
        drawer = DrawerBresenham(canvas)
        drawer.draw_model(model)
        frames.append(canvas)

    while True:
        for frame in frames + list(reversed(frames)):
            cv2.imshow('model', frame)
            cv2.waitKey(5)


if __name__ == "__main__":
    # tor_model()
    # head_model()
    head_model_rotating()
    wait_space_click()
