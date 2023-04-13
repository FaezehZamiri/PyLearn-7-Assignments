import cv2
import numpy as np

cap = cv2.VideoCapture('input/cars.mp4')
_,frame = cap.read()

result = np.zeros(frame.shape)
count = 0
while True:
    try:
        _,frame = cap.read()
        result += frame
        count += 1 
    except:
        break
    
result = result / count
cv2.imshow('',result)
cv2.imwrite('output/background_estimation.jpg',result)
cv2.waitKey()