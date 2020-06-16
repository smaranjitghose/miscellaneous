import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('WeedCont.tif', 0)

clahe = cv2.createCLAHE(clipLimit=6, tileGridSize=(8, 8))
claheImg = clahe.apply(img)

plt.title('CLAHE')
plt.imshow(claheImg)
plt.xticks([])
plt.yticks([])

plt.show()

# Better Implementation
def improve_contrast_image_using_clahe(bgr_image: np.array) -> np.array:
    hsv = open_cv.cvtColor(bgr_image, open_cv.COLOR_BGR2HSV)
    hsv_planes = open_cv.split(hsv)
    clahe = open_cv.createCLAHE(clipLimit=6.0, tileGridSize=(8, 8))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = open_cv.merge(hsv_planes)
    return open_cv.cvtColor(hsv, open_cv.COLOR_HSV2BGR)
