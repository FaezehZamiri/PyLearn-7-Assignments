import cv2

img_1 = cv2.imread('Input/1.jpg')
img_2 = cv2.imread('Input/2.jpg')

img_1 = cv2.cvtColor(img_1,cv2.COLOR_RGB2GRAY)
img_2 = cv2.cvtColor(img_2,cv2.COLOR_RGB2GRAY)
(row_1 , col_1)= img_1.shape
(row_2 , col_2) = img_2.shape

for i in range(row_1):
    for j in range(col_1):
        img_1[i,j] = 255 - img_1[i,j]

for i in range(row_2):
    for j in range(col_2):
        img_2[i,j] = 255 - img_2[i,j]

cv2.imshow('',img_1)
cv2.waitKey()
cv2.imshow('',img_2)
cv2.waitKey()

cv2.imwrite('Output/Invert_1.jpg',img_1)
cv2.imwrite('Output/Invert_2.jpg',img_2)