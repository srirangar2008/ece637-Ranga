import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from PIL import Image
import sys

def getGammaValue(grayval):
    gray = cm.get_cmap('gray', 256)
    checkerBoardPattern = np.array([[256, 256, 0 , 0], [256, 256, 0,0], [0,0,256,256], [0,0,256,256]])
    #plt.imshow(checkerBoardPattern, cmap=gray)
    #plt.show()

    tile_count = int(256/4)
    #plt.imshow(np.tile(np.tile(checkerBoardPattern, tile_count), (4,1)), cmap=gray)
    output = np.tile(np.tile(checkerBoardPattern, tile_count), (4,1))
    grays = (np.ones(16*256) * int(grayval)).reshape(16,256)
    output = np.concatenate((output, grays), axis=0)
    final_output = np.tile(output,(8,1))
    plt.imshow(final_output, cmap=gray)
    plt.title("Gray value = " + str(grayval))
    plt.show()

getGammaValue(sys.argv[1])

gray = cm.get_cmap('gray', 256)
im = Image.open("linear.tif")
plt.imshow(im, cmap=gray)
plt.title("Original Image - linear scaled")
plt.show()
x = np.array(im)
gamma = 1.99 
#set at 180.

y = np.array([(255 * (i/255)**(1/gamma)) for i in x.flatten()]).reshape((x.shape[0], x.shape[1])).astype(np.uint8)
plt.imshow(y, cmap=gray)
plt.title("Gamma scaled Image - Gamma = 1.99")
plt.show()


im2 = Image.open("gamma15.tif")
plt.imshow(im2, cmap=gray)
plt.title("Original Image - Gamma = 1.5")
plt.show()
x = np.array(im2)
gamma = 1.99 

y = np.array([(255 * (i/255)**(1.5/gamma)) for i in x.flatten()]).reshape((x.shape[0], x.shape[1])).astype(np.uint8)
plt.imshow(y, cmap=gray)
plt.title("Gamma scaled image - Gamma = 1.5/1.99")
plt.show()

