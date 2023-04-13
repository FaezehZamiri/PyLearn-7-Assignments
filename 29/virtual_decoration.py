import cv2

room_background = cv2.imread('input/room_background.jpg')
room_foreground = cv2.imread('input/room_foreground.jpg')
room_mask = cv2.imread('input/room_mask.webp')

#room_background = cv2.cvtColor(room_background,cv2.COLOR_RGB2GRAY)
#room_foreground = cv2.cvtColor(room_foreground,cv2.COLOR_RGB2GRAY)
#room_mask = cv2.cvtColor(room_mask,cv2.COLOR_RGB2GRAY)

room_mask =room_mask // 255

result1 = cv2.multiply(room_background , room_mask)
result2 = cv2.subtract(room_background , result1)
result3 = cv2.multiply(room_foreground , room_mask)

result = result2 + result3

cv2.imshow('',result)
cv2.imwrite('output/virtual_decoration.jpg',result)
cv2.waitKey()