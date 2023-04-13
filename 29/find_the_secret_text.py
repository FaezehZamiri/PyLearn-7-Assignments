import cv2

img_a = cv2.imread('input/a.png')
img_b = cv2.imread('input/b.png')

img_a = cv2.cvtColor(img_a,cv2.COLOR_RGB2GRAY)
img_b = cv2.cvtColor(img_b,cv2.COLOR_RGB2GRAY)

# subtract
result = cv2.subtract(img_b,img_a)

cv2.imshow('',result)
cv2.imwrite('output/secret_text.jpg',result)
cv2.waitKey()
