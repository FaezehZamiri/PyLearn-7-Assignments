import cv2

img_1 = cv2.imread('Input/1.jpg')
img_2 = cv2.imread('Input/2.jpg')

def Invert(img):
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    (row , col)= img.shape

    for i in range(row):
        for j in range(col):
            img[i,j] = 255 - img[i,j]

    cv2.imshow('',img)
    cv2.waitKey()
    return img

img_1=Invert(img_1)
img_2=Invert(img_2)
cv2.imwrite('Output/Invert_1.jpg',img_1)
cv2.imwrite('Output/Invert_2.jpg',img_2)
