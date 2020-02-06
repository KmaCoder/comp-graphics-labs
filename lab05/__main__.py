import numpy as np

from lab05.drawers import DrawerBresenham
from lab05.models.obj_model import ObjModel
from lab05.utils import wait_space_click


def head_model():
    height, width = 800, 800
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/materials/african_head.obj")
    model_canvas = np.zeros((height, width, 3), np.uint8)
    model_drawer = DrawerBresenham(model_canvas)
    obj_model.draw_model_filled(model_drawer)
    model_drawer.show_img("Head filled")


if __name__ == "__main__":
    head_model()
    wait_space_click()
