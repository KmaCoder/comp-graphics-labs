import sys

import cv2
import numpy as np
import lab01.config as cfg


class Vectorscope:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)
        self.result = np.zeros((cfg.out_dimension, cfg.out_dimension, 3), np.uint8)
        self.__draw_vectorscope()
        self.__draw_lines()

    def __draw_lines(self):
        size = cfg.out_dimension
        cv2.line(self.result, (size // 2, 0), (size // 2, size), cfg.line_color, 1)
        cv2.line(self.result, (0, size // 2), (size, size // 2), cfg.line_color, 1)
        cv2.circle(self.result, (size // 2, size // 2), size // 2, cfg.line_color, thickness=1)

    def __draw_vectorscope(self):
        out_size = cfg.out_dimension
        ycrcb_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2YCR_CB)
        height, width, channels = ycrcb_img.shape

        for i in range(height):
            progress_bar(i * width, height * width)
            for j in range(width):
                y = ycrcb_img.item(i, j, 0)
                cr = ycrcb_img.item(i, j, 1)
                cb = ycrcb_img.item(i, j, 2)
                new_i = out_size - int(cr / 255.0 * out_size)
                new_j = int(cb / 255.0 * out_size)
                self.result.itemset((new_i, new_j, 1), y)

    def show_img(self):
        cv2.imshow('image', self.result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def output_img(self, path):
        cv2.imwrite(path, self.result)


def progress_bar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '█' * int(round(percent * bar_length) - 1) + '█'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rProgress: |{0}| {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()
