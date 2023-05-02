import numpy as np
import cv2

img = cv2.imread('Input/lion.png',cv2.IMREAD_GRAYSCALE)#spider.webp

kernel= [[-1,-1,-1],
         [-1,8,-1],
         [-1,-1,-1]]
rows , cols = img.shape
result = np.zeros((rows,cols),dtype=np.uint8)

for i in range(1 , rows-1):
    for j in range(1 , cols-1):
        small = img[i-1:i+2 , j-1:j+2]
        result[i,j] = np.sum(small*kernel)

cv2.imshow('',result)
cv2.waitKey()
#cv2.imwrite('Output/Edge_Detection_2.jpg',result)
