import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('Input/6.jpg',cv2.IMREAD_GRAYSCALE)

while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    img[415:520,165:285] = frame[50:155,365:485]
    
    cv2.imshow('',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
