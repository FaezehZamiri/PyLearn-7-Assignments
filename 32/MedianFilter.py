import cv2
import numpy as np

img = cv2.imread('Input/a_noisy.png')

result1 = cv2.medianBlur(cv2.medianBlur(img,5),5)
result = np.hstack((img,result1))


cv2.imshow('',result)
cv2.imwrite('Output/MedianFilter6.jpg',result)
cv2.waitKey()
