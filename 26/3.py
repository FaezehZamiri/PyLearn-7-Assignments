import cv2

img = cv2.imread('Input/3.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow("",img)
cv2.waitKey()

cv2.imwrite('Output/Rotate.jpg',img)