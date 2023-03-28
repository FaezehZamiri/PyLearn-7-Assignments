import cv2

img = cv2.imread('Input/batman.webp')
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

rows , cols = img.shape 
threshold = 150
_,img = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY_INV)
cv2.putText(img,'BATMAN',(370,500),cv2.FONT_ITALIC,2,255,3)

cv2.imshow('',img)
cv2.waitKey()
cv2.imwrite("Output/batman.jpg",img)