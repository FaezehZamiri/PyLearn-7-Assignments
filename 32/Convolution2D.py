import cv2
import numpy as np

img = cv2.imread('Input/1.jpg',cv2.IMREAD_GRAYSCALE)

# 1. Edge detection filter
kernel1 = np.array([[-1 , -1 , -1],
                   [-1 ,  8 , -1],
                   [-1 , -1 , -1]])

# 2. Sharpening filter
kernel2 = np.array([[0  , -1 ,  0],
                   [-1 ,  5 , -1],
                   [0  , -1 ,  0]])

# 3. Emboss filter
kernel3 = np.array([[-2 , -1 ,  0],
                   [-1 ,  1 ,  1],
                   [0  ,  1 ,  2]])

# 4. Identity filter
kernel4 = np.array([[0  ,  0 ,  0],
                   [0  ,  1 ,  0],
                   [0  ,  0 ,  0]])

# 5. Your filter
kernel5 = np.array([[-1,0,-1],
                    [0,8,0],
                    [-1,0,-1]])


result1 = cv2.filter2D(img,-1,kernel1)
result2 = cv2.filter2D(img,-1,kernel2)
result3 = cv2.filter2D(img,-1,kernel3)
result4 = cv2.filter2D(img,-1,kernel4)
result5 = cv2.filter2D(img,-1,kernel5)

result = np.hstack((img,result1,result2,result3,result4,result5))
cv2.imwrite('Output/convolution2d.jpg',result)
cv2.imshow('',result)
cv2.waitKey()