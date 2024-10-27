import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

#generar datos 
np.random.seed(42)

points= 100
x= np.random.rand(points)
y= np.random.rand(points)
z= np.random.rand(points)

#la figura 3d
plot = plt.figure(figsize=(8,6))

#agregar un subplto 3d
ax = plot.add_subplot(111, projection="3d")

#creas grafico de dispersi9on
ax.scatter(x,y,z, c="blue", marker="p") # s / p

ax.set_xlabel("eje x")
ax.set_ylabel("eje y")
ax.set_zlabel("eje z")
ax.set_title("scatter plot 3d")

plt.show()