import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import cmath

input_array = np.zeros((256,256))
input_array[127][127] = 1
output_array = np.zeros((256,256))

for i in range(0,256):
    for j in range(0,256):
        output_array[i][j] = 0.01 * input_array[i][j]
        if(i > 0):
            output_array[i][j] += 0.9 * output_array[i - 1][j]
        if(j > 0):
            output_array[i][j] += 0.9 * output_array[i][j - 1]
        if(i > 0 and j > 0):
            output_array[i][j] -= 0.81 * output_array[i - 1][j - 1]

im_save = Image.fromarray((255 * 100 * output_array).astype(np.uint8))
im_save.save("h_out.tif")


x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)

def genComplexArray(m,n):
    return (np.arange(m) * 0j)[:, None] + np.arange(n)
z = genComplexArray(1024, 1024)
X, Y = np.meshgrid(x,y)

for m in range(0,len(x)) :
    for n in range(0,len(y)) : 
        z[m][n] = 1 / (1 - (0.9 * cmath.exp(complex(0,-x[m]))) - (0.9 * cmath.exp(complex(0,-y[n]))) + 0.81 * (cmath.exp(complex(0,-(x[m] + y[n])))))
Z = abs(z)
fig = plt.figure(1)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Magnitude of H")

Z = np.angle(z)
fig = plt.figure(2)
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Phase of H")

plt.show()
    
