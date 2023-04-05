import cv2
import numpy as np

img = np.zeros((400,600,3))

for j in range(6):
    if np.mod(j,2)==0:
        img[:,j*100:(j+1)*100,0] = 71
        img[:,j*100:(j+1)*100,1] = 141
        img[:,j*100:(j+1)*100,2] = 17
    else:
        img[:,j*100:(j+1)*100,0] = 63
        img[:,j*100:(j+1)*100,1] = 122
        img[:,j*100:(j+1)*100,2] = 13

#point = [col,row]
cv2.rectangle(img,[20,20],[600-20,400-20],[255,255,255],3)

cv2.rectangle(img,[20,100],[140,300],[255,255,255],3)
cv2.rectangle(img,[20,150],[70,250],[255,255,255],3)

cv2.rectangle(img,[600-20,100],[600-140,300],[255,255,255],3)
cv2.rectangle(img,[600-20,150],[600-70,250],[255,255,255],3)

cv2.line(img,[600//2,20],[600//2,400-20],[255,255,255],3)

cv2.circle(img,[600//2,400//2],70,[255,255,255],3)
cv2.circle(img,[600//2,400//2],4,[255,255,255],3)

cv2.imwrite('Output/Football_Pitch.jpg',img)
cv2.imshow('',img)
cv2.waitKey()