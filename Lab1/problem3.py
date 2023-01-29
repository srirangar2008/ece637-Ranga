import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import scipy.signal
from matplotlib import cm

h = (1/81) * np.ones((9,9))
fft_out = np.fft.fft2(h, s=[1024,1024])
fft_out = np.fft.fftshift(fft_out)

#plt.plot(np.linspace(-512, 512, 1024), abs(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = abs(fft_out)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Magnitude of H")
#plt.show()

##plt.plot(np.linspace(-np.pi, np.pi, 1024), np.angle(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = np.angle(fft_out)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Phase of H")
plt.show()









