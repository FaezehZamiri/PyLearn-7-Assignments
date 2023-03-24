import cv2

img = cv2.imread('Output/Invert_1.jpg')
img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)

for i in range(240):
    for j in range(140-i,240-i):
        if j >= 0:
            img[i,j] = 0

cv2.imshow('',img)
cv2.waitKey()
cv2.imwrite('Output/DeathSymbol.jpg',img)