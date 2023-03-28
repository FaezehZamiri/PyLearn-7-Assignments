import time
import cv2
import imageio
import numpy as np

rows = np.random.random((1,500))*666
#cols = np.random.random((1,500))*1000
cols = [i for i in range(1,1000,2)]
rows = np.array(rows , dtype=np.uint0)
cols = np.array(cols , dtype=np.uint0)
images = []

while True:
    img = cv2.imread('Input/winter.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    for i in range(500):
        r = int(rows[0][i])
        c = int(cols[i])
        img[r:int(r+2),c:int(c+2)] = 255   

    for i in range(500):
        rows[0][i] = rows[0][i] + 100
        if rows[0][i] > 666:
            rows[0][i] = rows[0][i]-666
    
    cv2.imshow('',img)
    time.sleep(0.8)
    images.append(img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

imageio.mimsave('Output/winter.gif',images)