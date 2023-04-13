import cv2

img = cv2.imread('input/person.jpg',cv2.IMREAD_GRAYSCALE)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted,[21,21],0)
inverted_blurred = 255 - blurred

sketch = img / inverted_blurred
sketch = sketch * 255

cv2.imshow('',sketch)
cv2.imwrite('output/photo_to_sketch.jpg',sketch)
cv2.waitKey()
