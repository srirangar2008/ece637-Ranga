import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image

def stretch(input_img, T1, T2):
    input = input_img.flatten()
    print(input.shape)
    output = np.zeros(input.shape)
    for i in range(0, len(input )):
        if input[i] < T1:
            output[i] = 0
        elif input[i] > T2 :
            output[i] = 255
        else : 
            output[i] = ((255 * (input[i] - T1)) / (T2 - T1))
    output = output.astype(np.uint8)
    output_img = output.reshape((input_img.shape[0], input_img.shape[1]))
    plt.imshow(output_img, cmap=gray)
    plt.title("Stretched Image")
    plt.show()
    return output_img


gray = cm.get_cmap('gray', 256)
im2 = Image.open("kids.tif")
x = np.array(im2)
plt.hist(x.flatten(), bins=np.linspace(0,255,256))

plt.title("Histogram of kids.tif")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of pixels")
plt.show()

height, width = np.histogram(x.flatten(), bins=np.linspace(0,255,256))
print(len(height))
print(len(width))
plt.plot(np.linspace(0,255,len(height)), height)
plt.show()

height, width = np.histogram(x.flatten(), bins=np.linspace(0,255,256))
output_img = stretch(x, 70, 180)
plt.hist(output_img.flatten(), bins=np.linspace(0,255,256))
plt.title("Histogram of the stretched image")
plt.show()