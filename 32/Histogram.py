import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Input/hist1.jpg',cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

# equalized
img2 = cv2.equalizeHist(img)
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

# clahe
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img2)
hist3 = cv2.calcHist([cl1],[0],None,[256],[0,256])

# plot

plt.subplot(3,2,1)
plt.imshow(img,cmap='gray')
plt.title('Input Image')
plt.subplot(3,2,2)
plt.plot(hist)


plt.subplot(3,2,3)
plt.imshow(img2,cmap='gray')
plt.title('Equalized Image')
plt.subplot(3,2,4)
plt.plot(hist2)



plt.subplot(3,2,5)
plt.imshow(cl1,cmap='gray')
plt.title('Apply Clahe')
plt.subplot(3,2,6)
plt.plot(hist3)
plt.show()

