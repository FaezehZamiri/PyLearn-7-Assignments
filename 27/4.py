import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    cv2.rectangle(frame,(270,190),(370,290),0,6)
    box = frame[187:294,267:374]
    blur_frame = cv2.medianBlur(frame,31)
    blur_frame[187:294,267:374] = box

    if np.mean(box) <= 50:
        text = "balck"
    elif np.mean(box) >= 150:
        text = "white"
    else:
        text = "gray"
    cv2.putText(blur_frame,text,(20,60),cv2.FONT_ITALIC,1,0,2)
    
    cv2.imshow('',blur_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

