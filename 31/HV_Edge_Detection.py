import numpy as np
import cv2

img = cv2.imread('Input/building.png',cv2.IMREAD_GRAYSCALE)

horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s2
vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # s1

rows , cols = img.shape
result = np.zeros((rows,cols),dtype=np.uint8)
newhorizontalImage = np.zeros((rows,cols),dtype=np.uint8)
newverticalImage = np.zeros((rows,cols),dtype=np.uint8)

for i in range(1 , rows-1):
    for j in range(1 , cols-1):
        horizontalGrad = (horizontal[0, 0] * img[i - 1, j - 1]) + \
                         (horizontal[0, 1] * img[i - 1, j]) + \
                         (horizontal[0, 2] * img[i - 1, j + 1]) + \
                         (horizontal[1, 0] * img[i, j - 1]) + \
                         (horizontal[1, 1] * img[i, j]) + \
                         (horizontal[1, 2] * img[i, j + 1]) + \
                         (horizontal[2, 0] * img[i + 1, j - 1]) + \
                         (horizontal[2, 1] * img[i + 1, j]) + \
                         (horizontal[2, 2] * img[i + 1, j + 1])

        newhorizontalImage[i-1 , j-1] = abs(horizontalGrad)

        verticalGrad = (vertical[0, 0] * img[i - 1, j - 1]) + \
                       (vertical[0, 1] * img[i - 1, j]) + \
                       (vertical[0, 2] * img[i - 1, j + 1]) + \
                       (vertical[1, 0] * img[i, j - 1]) + \
                       (vertical[1, 1] * img[i, j]) + \
                       (vertical[1, 2] * img[i, j + 1]) + \
                       (vertical[2, 0] * img[i + 1, j - 1]) + \
                       (vertical[2, 1] * img[i + 1, j]) + \
                       (vertical[2, 2] * img[i + 1, j + 1])

        newverticalImage[i-1, j-1] = abs(verticalGrad)

        # Edge Magnitude
        mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
        result[i-1 , j-1] = mag

cv2.imshow('',result)
cv2.waitKey()
cv2.imwrite('Output/Edge_Detection_3.jpg',result)
