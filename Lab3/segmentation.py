import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl

im = Image.open("output_segment_T_1.tif")

x=np.array(im)

N = np.max(x)

cmap = mpl.colors.ListedColormap(np.random.rand(N+1,3))
plt.imshow(x, cmap=cmap, interpolation='none')
plt.colorbar()
plt.title('Image T=1')
plt.show()

im = Image.open("output_segment_T_2.tif")

x=np.array(im)

N = np.max(x)

cmap = mpl.colors.ListedColormap(np.random.rand(N+1,3))
plt.imshow(x, cmap=cmap, interpolation='none')
plt.colorbar()
plt.title('Image T=2')
plt.show()

im = Image.open("output_segment_T_3.tif")

x=np.array(im)

N = np.max(x)

cmap = mpl.colors.ListedColormap(np.random.rand(N+1,3))
plt.imshow(x, cmap=cmap, interpolation='none')
plt.colorbar()
plt.title('Image T=3')
plt.show()


