import numpy as np                 # Numpy is a library support computation of large, multi-dimensional arrays and matrices.
from PIL import Image              # Python Imaging Library (abbreviated as PIL) is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.
import matplotlib.pyplot as plt    # Matplotlib is a plotting library for the Python programming language.



def BetterSpecAnalyzer(image):
    [h, w] = image.shape
    print("h = " + str(h) + ", w = " + str(w))
    midh = int(h / 2)
    midw = int(w / 2)
    #25 filters to be used. 5 * 5
    N = 64 #size of each filter 
    print(midh, midw)
    H = np.outer(np.hamming(64), np.hamming(64))
    print(H.shape)
    X = np.double(image)/255

    #overlapping
    start_h = int(midh - ((N*5)/2))
    start_w = int(midw - ((N*5)/2))

    Z = np.zeros((512, 512))

    for i in range(0,5):
        for j in range(0,5):
            h_start = start_h + i*N
            h_end = start_h + (i+1)*N
            w_start = start_w + j*N
            w_end = start_w + (j+1)*N
            print('h_start = ' , h_start , ' , h_end = ', h_end, ' , w_start = ', w_start, ' , w_end = ', w_end)
            z = X[h_start : h_end, w_start : w_end]
            z_hamm = z*H
            Z = Z + (1/N**2) * abs(np.fft.fftshift(np.fft.fft2(z_hamm, s=[512, 512]))**2)
    
    Z = Z / 25
    # Compute the logarithm of the Power Spectrum.
    Zabs = np.log(Z)
    # Plot the result using a 3-D mesh plot and label the x and y axises properly. 
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    a = b = np.linspace(-np.pi, np.pi, num = 512)
    X, Y = np.meshgrid(a, b)

    surf = ax.plot_surface(X, Y, Zabs, cmap=plt.cm.coolwarm)
    #ax = plt.axes(projection='3d')
    #ax.contour3D(X, Y, Zabs, 50, cmap='viridis')

    ax.set_xlabel('$\mu$ axis')
    ax.set_ylabel('$\\nu$ axis')
    ax.set_zlabel('Z Label')

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

# Read in a gray scale TIFF image.
im = Image.open('img04g.tif')
# Import Image Data into Numpy array.
# The matrix x contains a 2-D array of 8-bit gray scale values. 
x = np.array(im)
print('Data type: ', x.dtype)
x = np.double(x)/255.0
BetterSpecAnalyzer(x)

