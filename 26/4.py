import cv2
import numpy as np

img = np.zeros((600,600))

img[0:75,150:450] = 255
img[:,150:225] = 255
img[225:300,150:420] = 255 

for i in range(600):
    for j in range(600):
        img[i,j] = 255 - img[i,j]
cv2.imshow('F',img)
cv2.waitKey()
cv2.imwrite('Output/F.jpg',img)