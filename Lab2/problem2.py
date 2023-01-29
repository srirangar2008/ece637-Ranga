import numpy as np              
from PIL import Image
import matplotlib.pyplot as plt
import cmath 
import BetterSpectrumAnalyzer

image = np.random.uniform(low=-0.5, high=0.5, size=(512,512))
image_scaled = (image + 0.5) * 255
plt.imshow(np.uint8(image_scaled), cmap=plt.cm.gray)
plt.title('Image')
plt.show()
# Import Image Data into Numpy array.
# The matrix x contains a 2-D array of 8-bit gray scale values. 

x_scaled = np.array(image_scaled)
img_out = Image.fromarray(x_scaled.astype(np.uint8))

img_out.save('random.tif')
x = np.array(image)
print('Data type: ', x.dtype) 

#The filter difference equation
#y(m,n) = 3x(m,n) + 0.99y(m-1,n) + 0.99y(m,n-1) - 0.9801y(m-1,n-1)

m,n = x.shape
print(x.shape)
y = np.zeros((m,n))
for i in range(0,m):
    for j in range(0,n):
        y[i][j] = 3 * x[i][j]
        if(i > 0):
            y[i][j] = y[i][j] + (0.99 * y[i-1][j])
        if(j > 0):
            y[i][j] = y[i][j] + (0.99 * y[i][j-1])
        if(i > 0 and j > 0):
            y[i][j] = y[i][j] - (0.9801 * y[i-1][j-1])

out_img = y
y = np.uint8(y + 127)
print('after uint8 = ')
print(y)
plt.imshow(y, cmap=plt.cm.gray)
plt.title('Image')
plt.show()

img_out_2 = Image.fromarray(y.astype(np.uint8))
img_out_2.save('filter_random.tif')


x = np.linspace(-np.pi, np.pi, 1024)
y = np.linspace(-np.pi, np.pi, 1024)

def genComplexArray(m,n):
    return (np.arange(m) * 0j)[:, None] + np.arange(n)
z = genComplexArray(1024, 1024)
X, Y = np.meshgrid(x,y)



for m in range(0,len(x)) :
    for n in range(0,len(y)) : 
        z[m][n] = 3 / (1 - (0.99 * cmath.exp(complex(0,-x[m]))) - (0.99 * cmath.exp(complex(0,-y[n]))) + 0.9801 * (cmath.exp(complex(0,-(x[m] + y[n])))))
Z = np.log((abs(z)**2)/12)
fig = plt.figure(1)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.coolwarm)

ax.set_xlabel('$\mu$ axis')
ax.set_ylabel('$\\nu$ axis')
ax.set_zlabel('Z Label')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

BetterSpectrumAnalyzer.BetterSpecAnalyzer(out_img)
