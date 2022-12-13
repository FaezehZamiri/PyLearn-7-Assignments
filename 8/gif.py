import os
import imageio

myfiles=os.listdir('images')
images=[]
for i in range(len(myfiles)):
    image=imageio.imread("images"+'/'+myfiles[i])
    images.append(image)

imageio.mimsave("mygif.gif",images)