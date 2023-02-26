import numpy as np
import cv2


# 定义图像增强函数
def image_augment(image):
    # 随机旋转图像
    angle = np.random.randint(-10, 10)
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    image = cv2.warpAffine(image, M, (cols, rows))

    # 随机翻转图像
    flip_code = np.random.randint(-1, 2)
    image = cv2.flip(image, flip_code)

    return image
