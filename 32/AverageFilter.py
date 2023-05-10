import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Input/1.tif',cv2.IMREAD_GRAYSCALE)


kernel_1 = np.ones((5, 5), np.float32)/0.04
kernel_2 = np.ones((5, 5), np.float32)/1
kernel_3 = np.ones((5, 5), np.float32)/5
kernel_4 = np.ones((3, 3), np.float32)/0.04
kernel_5 = np.ones((3, 3), np.float32)/1
kernel_6 = np.ones((3, 3), np.float32)/5
kernel_7 = np.ones((3, 3), np.float32)/3

result_1 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_1)
result_2 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_2)
result_3 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_3)
result_4 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_4)
result_5 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_5)
result_6 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_6)
result_7 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_7)

plt.subplot(2,4,1)
plt.title('Iuput Image')
plt.imshow(img,cmap='gray')

plt.subplot(2,4,2)
plt.title('Kernel 5*5 : 0.04')
plt.imshow(result_1,cmap='gray')

plt.subplot(2,4,3)
plt.title('Kernel 5*5 : 1')
plt.imshow(result_2,cmap='gray')

plt.subplot(2,4,4)
plt.title('Kernel 5*5 : 5')
plt.imshow(result_3,cmap='gray')

plt.subplot(2,4,5)
plt.title('Kernel 3*3 : 0.04')
plt.imshow(result_4,cmap='gray')

plt.subplot(2,4,6)
plt.title('Kernel 3*3 : 1')
plt.imshow(result_5,cmap='gray')

plt.subplot(2,4,7)
plt.title('Kernel 3*3 : 5')
plt.imshow(result_6,cmap='gray')

plt.subplot(2,4,8)
plt.title('Kernel 3*3 : 3')
plt.imshow(result_7,cmap='gray')
plt.show()
