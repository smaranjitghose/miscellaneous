import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("demo.jpeg")


def improve_contrast_image_using_clahe(bgr_image: np.array, clipLimit: float = 5.0) -> np.array:
    hsv_img = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    hsv_planes = cv2.split(hsv_img)
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=(8, 8))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv_img = cv2.merge(hsv_planes)
    return cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
