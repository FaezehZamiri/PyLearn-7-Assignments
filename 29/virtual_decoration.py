import cv2
import numpy as np

room_background = cv2.imread('input/room_background.jpg')
room_foreground = cv2.imread('input/room_foreground.jpg')
room_mask = cv2.imread('input/room_mask.webp')

room_background = room_background.astype(np.float32)
room_foreground = room_foreground.astype(np.float32)
room_mask = room_mask.astype(np.float32)

room_mask = room_mask / 255

result1 = cv2.multiply(room_background , room_mask)
result2 = cv2.subtract(room_background , result1)
result3 = cv2.multiply(room_foreground , room_mask)

result = cv2.add(result2 , result3)

result = result.astype(np.uint8)
cv2.imshow('',result)
cv2.imwrite('output/virtual_decoration.jpg',result)
cv2.waitKey()
