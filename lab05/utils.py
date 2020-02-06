import cv2


def wait_space_click():
    while True:
        k = cv2.waitKey(33)
        if k == 32:
            break
