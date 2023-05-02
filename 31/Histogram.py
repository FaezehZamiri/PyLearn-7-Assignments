import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('Input/girls.jpg')
lum_img = img[:, :, 0]

plt.subplot(2,2,1)
plt.title('Input Image')
plt.imshow(img)

# Use plt.hist()
plt.subplot(2,2,2)
plt.title('Histogram with Matplotlib')
plt.hist(lum_img.ravel(), bins=range(256), fc='k', ec='k')


# Use function
def Histogram(lum_img):
    row,col = lum_img.shape
    img_array = np.reshape(lum_img,-1)
    img_array = np.sort(img_array)

    hist = np.zeros(256)
    count = 0
    for i in range(row*col):
        count = img_array[i]
        hist[count] += 1
    return hist

hist = Histogram(lum_img)

plt.subplot(2,2,3)
plt.title('BarPlot with Matplotlib')
plt.bar(np.arange(256),hist)

plt.subplot(2,2,4)
plt.plot(hist)
plt.title('Histogram with Function')
plt.show()

