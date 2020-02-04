import sys

import cv2
import numpy as np
import lab01.config as cfg


class Vectorscope:
    def __init__(self, img_name):
        self.img = cv2.imread(cfg.IO_path + img_name)
        self.ycrcb_img = self._to_ycrcb(self.img)
        self.vectrorscope_img = np.zeros((cfg.out_dimension, cfg.out_dimension, 3), np.uint8)
        self._draw_vectorscope()
        self._draw_lines()

    @staticmethod
    def _to_ycrcb(img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

    def _draw_lines(self):
        size = cfg.out_dimension
        cv2.line(self.vectrorscope_img, (size // 2, 0), (size // 2, size), cfg.line_color, 1)
        cv2.line(self.vectrorscope_img, (0, size // 2), (size, size // 2), cfg.line_color, 1)
        cv2.circle(self.vectrorscope_img, (size // 2, size // 2), size // 2, cfg.line_color, thickness=1)

    def _draw_vectorscope(self):
        out_size = cfg.out_dimension
        height, width, channels = self.ycrcb_img.shape

        for i in range(height):
            progress_bar(i * width, height * width)
            for j in range(width):
                y = self.ycrcb_img.item(i, j, 0)
                cr = self.ycrcb_img.item(i, j, 1)
                cb = self.ycrcb_img.item(i, j, 2)
                new_i = out_size - int(cr / 255.0 * out_size)
                new_j = int(cb / 255.0 * out_size)
                self.vectrorscope_img.itemset((new_i, new_j, 1), y)

    def show_result(self):
        cv2.imshow('ycrcb', self.ycrcb_img)
        cv2.imshow('vectorscope', self.vectrorscope_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def output_result(self):
        cv2.imwrite(cfg.IO_path + "out_ycrcb.jpg", self.ycrcb_img)
        cv2.imwrite(cfg.IO_path + "out_vectorscope.jpg", self.vectrorscope_img)


def progress_bar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '█' * int(round(percent * bar_length) - 1) + '█'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rProgress: |{0}| {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()
