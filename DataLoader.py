import os

import cv2
import numpy as np


class DataLoader:

    def __init__(self, path=".."):
        self.path_tampered_i = path + "/train" + "/tampered" + "/imgs"
        self.path_tampered_m = path + "/train" + "/tampered" + "/masks"
        self.path_untampered_i = path + "/train" + "/untampered"
        self.path_test = path + "/test" + "/imgs"

    def getTamperedImages(self):
        images = []
        for filename in os.listdir(self.path_tampered_i):
            img = cv2.imread(os.path.join(self.path_tampered_i, filename))
            if img is not None:
                images.append(img)

        return images

    def getTamperedMasks(self):
        images = []
        for filename in os.listdir(self.path_tampered_m):
            img = cv2.imread(os.path.join(self.path_tampered_m, filename))
            if img is not None:
                images.append(img)

        return images

    def getUntamperedImages(self):
        images = []
        i = 0  # 内存不够，中断措施
        for filename in os.listdir(self.path_untampered_i):
            i = i + 1
            if i == 3:
                break
            img = cv2.imread(os.path.join(self.path_untampered_i, filename))
            print(filename)
            if img is not None:
                images.append(img)

        return images

    def getTestImages(self):
        images = []
        for filename in os.listdir(self.path_test):
            img = cv2.imread(os.path.join(self.path_test, filename))
            if img is not None:
                images.append(img)

        return images


