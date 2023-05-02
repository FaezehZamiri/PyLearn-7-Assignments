import numpy as np
import cv2

img = cv2.imread('Input/flower_input.jpg',cv2.IMREAD_GRAYSCALE)

kernel_1 = np.ones((11, 11), np.float32)/121
img_1 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_1)

rows , cols = img.shape
result = np.zeros((rows,cols),dtype=np.uint8)
t = (11-1)//2
for i in range(t , rows-t):
    for j in range(t , cols-t):
        if img[i,j] < 130:
            small = img[i-t:i+t+1 , j-t:j+t+1]
            result[i,j] = np.sum(small*kernel_1)
        else:
            result[i,j] = img[i,j]

cv2.imshow('',result)
cv2.waitKey()
cv2.imwrite('Output/Blur.jpg',result)


