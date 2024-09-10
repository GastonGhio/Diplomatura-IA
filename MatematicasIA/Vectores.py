import numpy as np
import matplotlib.pyplot as plt


# generaremos un vector de 3 dimensiones

vectorNumpy = np.array([1.2, 5, 13])
print(vectorNumpy)

print(vectorNumpy.size)

print(vectorNumpy[2])


#generaremos dos vectores en 2 dimensiones para graficar 

u = np.array([6, 5])
v = np.array([8, 1])

x, y = zip(u, v) #crea 2 tuplas el metodo zip a partir de dos arreglos
plt.scatter(x, y, color=["r","b"]) #es la generacion del grafico
plt.grid() #crea una cuadricula en el grafico
plt.show()