import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('WeedCont.tif', 0)

clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
claheImg = clahe.apply(img)

plt.title('CLAHE')
plt.imshow(claheImg)
plt.xticks([])
plt.yticks([])

plt.show()
