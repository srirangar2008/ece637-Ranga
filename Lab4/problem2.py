import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

def equalize(image) : 
    gray = cm.get_cmap('gray', 256)
    im = Image.open(image)
    x = np.array(im)
    plt.imshow(im, cmap=gray)
    plt.title("Original image")
    plt.show()
    height_im, width_im = x.shape
    print(height_im, width_im)
    height, width = np.histogram(x.flatten(), bins=np.linspace(0,255,256))
    print(len(height))
    total_sum = sum(height)
    print('Sum = ', total_sum)
    cdf = np.zeros((256, 1))
    value = 0.0
    for i in range(0,len(height)):
        value += height[i]
        cdf[i] = value / total_sum
    plt.plot(np.linspace(0,255,255), cdf[0:255])
    plt.title("F_x[i] of the image")
    plt.xlabel("Pixel intenisty")
    plt.ylabel("Probability of the pixel intensity")
    plt.show()
    Y_s = [cdf[i] for i in x.flatten()]
    
    
    print(len(Y_s))
    min_ys = min(Y_s)
    max_ys = max(Y_s)
    print(min_ys, max_ys)
    Z_s = [((255)*((Y_s[i] - min_ys)/(max_ys - min_ys))) for i in range(0, len(Y_s))]
    Z_image = np.reshape(Z_s, (height_im, width_im))
    plt.imshow(Z_image, cmap=gray)
    plt.title("Equalized image")
    plt.show()
    plt.hist(Z_image.flatten(), bins=np.linspace(0,255,256))
    plt.title("Histogram of the equalized image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of pixels")
    plt.show()
    #for i in range(0,len(height)):

equalize("kids.tif")