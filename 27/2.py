import cv2
import imageio
import numpy as np

images = []
while True:
    img = np.random.random((250,350))*255
    img = np.array(img , dtype=np.uint8)
    images.append(img)
    cv2.imshow('',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

imageio.mimsave('Output/tv.gif',images)