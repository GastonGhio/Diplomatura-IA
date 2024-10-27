import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from sklearn.datasets import load_iris

#cargar datos de iris
iris = load_iris()
data= iris.data 
target = iris.target

#cread grafico
plot= plt.figure(figsize=(8,6))
ax = plot.add_subplot(111 , projection="3d")

ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=target, cmap='viridis', marker='s')

ax.set_xlabel("Sepal Length (cm)")
ax.set_ylabel("Sepal Width (cm)")
ax.set_zlabel("Petal Length (cm)")
ax.set_title("Iris Dataset - 3D Scatter Plot")

plt.show()

