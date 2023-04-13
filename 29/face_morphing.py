import cv2
import numpy as np

human_img = cv2.imread('input/1.jpg')
animal_img  = cv2.imread('input/2.jpg')

human_img = human_img.astype(np.float32)
animal_img = animal_img.astype(np.float32)

result_1 = human_img * 2/3 + animal_img * 1/3
result_2 = human_img * 1/2 + animal_img * 1/2
result_3 = human_img * 1/3 + animal_img * 2/3

row , col , band = result_1.shape
result = np.zeros((row,col*5,band))

result[:,:col,:] = human_img
result[:,col:2*col,:] = result_1
result[:,2*col:3*col,:] = result_2
result[:,3*col:4*col,:] = result_3
result[:,4*col:,:] = animal_img

result = result.astype(np.uint8)
cv2.imshow('',result)
cv2.imwrite('output/face_morphing.jpg',result)
cv2.waitKey()