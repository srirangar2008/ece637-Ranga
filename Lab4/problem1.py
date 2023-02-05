import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

gray = cm.get_cmap('gray', 256)
im1 = Image.open("race.tif")
x = np.array(im1)
#plt.imshow(x, cmap=gray)
#plt.show()
plt.hist(x.flatten(), bins=np.linspace(0,255,256))
plt.title("Histogram of race.tif")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of pixels")
plt.show()

im2 = Image.open("kids.tif")
x1 = np.array(im2)
plt.hist(x1.flatten(), bins=np.linspace(0,255,256))

plt.title("Histogram of kids.tif")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of pixels")
plt.show()

height, width = np.histogram(x1.flatten(), bins=np.linspace(0,255,256))
print(len(height))
print(len(width))
plt.plot(np.linspace(0,255,len(height)), height)
plt.show()





