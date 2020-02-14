from time import time

import cv2
import numpy as np

from lab06.drawers import DrawerBresenham
from lab06.models.torus import Torus
from lab06.utils import wait_space_click


def tor_model():
    height, width = 600, 600
    model = Torus(R=200, r=100, vertices_count=50)
    canvas = np.zeros((height, width, 3), np.uint8)
    drawer = DrawerBresenham(canvas)
    drawer.draw_model(model)
    drawer.show_img("Tor")


def tor_model_rotating():
    height, width = 600, 600
    model = Torus(R=200, r=100, vertices_count=40)
    model.rotate(40, 0, 10)
    model.translate(np.array([300, 300, 1000]))

    frames = []
    frames_len = 30
    for i in range(frames_len):
        print(f'\rRendering frame: {i + 1}/{frames_len}', end='')
        model.rotate(0, 5, 5)
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
    tor_model_rotating()
    wait_space_click()
