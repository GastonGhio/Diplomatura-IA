import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # este modulo permite trabajar con modelos 3d es de matplot

a = np.array([3,4,6])
b = np.array([4,7,1])

c = np.array([3,5,3])








#creamos subplot 3d
subplot= plt.subplot(111, projection = "3d") #111 significa 1 fila 1 xcolumna primer subplot

#definir coordenadas
x_coords, y_coords, z_coords = zip(a,b,c) # funcion zip agarra de las variables a y b las coordenadas

#graficamos los puntos
subplot.scatter(x_coords,y_coords,z_coords)

#establecemos los mlimites, es esto nesesario?
subplot.set_zlim3d([0,10])

plt.show()

