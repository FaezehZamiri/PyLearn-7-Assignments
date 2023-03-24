import cv2
import numpy as np

img = np.zeros((256,256))

for j in range(256):
    for i in range(256):
        img[i,j] = 255 - i

cv2.imwrite('Output/Gradient.jpg',img)