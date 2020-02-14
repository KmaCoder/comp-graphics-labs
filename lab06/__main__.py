import cv2
import numpy as np

from lab06.drawers import DrawerBresenham
from lab06.models.obj3d import ObjModel
from lab06.models.torus import Torus


def model_rotating(model: ObjModel):
    height, width = 600, 600

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
            cv2.imshow('Model rotating', frame)
            cv2.waitKey(5)


def head():
    head_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj",
                          set_scaled=True)
    head_model.rotate(20, 0, 5)
    model_rotating(head_model)


def tor():
    tor_model = Torus(R=200, r=100, vertices_count=40, set_scaled=False)
    tor_model.rotate(40, 0, 10)
    tor_model.translate(np.array([300, 300, 1000]))
    model_rotating(tor_model)


if __name__ == "__main__":
    tor() # lab06
    # head()  # lab07
