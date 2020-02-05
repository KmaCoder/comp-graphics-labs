import numpy as np

from lab03.drawers import DrawerBresenham, DrawerCV2
from lab03.models.obj_model import ObjModel
from lab03.utils import wait_space_click


def head_model():
    height, width = 600, 600
    obj_model = ObjModel("/Users/kmacoder/Mohylyanka/4-course/comp_graphics/lab02/materials/african_head.obj")

    model_canvas = np.zeros((height, width, 3), np.uint8)
    model_drawer = DrawerBresenham(model_canvas)
    obj_model.draw_model_filled(model_drawer)
    model_drawer.show_img("Head filled")

    model_canvas_cv2 = np.zeros((height, width, 3), np.uint8)
    model_drawer_cv2 = DrawerCV2(model_canvas_cv2)
    obj_model.draw_model_filled(model_drawer_cv2)
    model_drawer_cv2.show_img("Head filled CV2")


if __name__ == "__main__":
    head_model()
    wait_space_click()
