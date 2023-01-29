import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft
import scipy.signal
from matplotlib import cm

h = (1/25) * np.ones((5,5))

fft_out = np.fft.fft2(h, s=[1024,1024])
fft_out = np.fft.fftshift(fft_out)

#plt.plot(np.linspace(-512, 512, 1024), abs(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = abs(fft_out)
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Magnitude of H")
#plt.show()

#plt.plot(np.linspace(-np.pi, np.pi, 1024), np.angle(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = np.angle(fft_out)
fig = plt.figure(2)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Phase of H")
#plt.show()


g = np.zeros((5,5))
lambda_var = 1.5
delta = 0;
for i in range(0,5):
    for j in range(0,5):
        if(i == 2 and j == 2):
            delta = 1
        else:
            delta = 0
        g[i][j] = delta + lambda_var*(delta - h[i][j])

fft_out = np.fft.fft2(g, s=[1024,1024])
fft_out = np.fft.fftshift(fft_out)

#plt.plot(np.linspace(-512, 512, 1024), abs(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = abs(fft_out)
fig = plt.figure(3)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Magnitude of G")
#plt.show()

#plt.plot(np.linspace(-np.pi, np.pi, 1024), np.angle(fft_out[1]))
#plt.show()

x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)
X, Y = np.meshgrid(x,y)
Z = np.angle(fft_out)
fig = plt.figure(4)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Phase of G")
plt.show()









