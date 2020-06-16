import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('demo.jpeg', 0)

clahe = cv2.createCLAHE(clipLimit=6, tileGridSize=(8, 8))
claheImg = clahe.apply(img)

plt.title('CLAHE')
plt.imshow(claheImg)
plt.xticks([])
plt.yticks([])

plt.show()

# Better Implementation
def improve_contrast_image_using_clahe(bgr_image: np.array) -> np.array:
    hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    hsv_planes = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=6.0, tileGridSize=(8, 8))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
