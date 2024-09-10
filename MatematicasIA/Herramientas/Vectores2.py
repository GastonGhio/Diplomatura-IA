import matplotlib.pyplot as plt
import numpy as np


def plotVector (vector, origin=[0,0], **option):
    
    return plt.arrow(origin[0], origin[1], vector[0], vector[1], head_width=0.5, head_length = 0.4, length_includes_head=True, **option)

#definir vectores
u = np.array([0, 5])
v = np.array([5, 0])
z = np.array([0, -5])
x = np.array([-5,0])

a = np.array([1,1])
b = np.array([1,2])
c = np.array([2,3])
d = np.array([8,4])

#graficar vectores llamo a la funcion
plotVector(a, color="r")
plotVector(b, color="b")
plotVector(c, color="g")
plotVector(d, color="black")

 #traza los limites del eje X y el Y
plt.axis([-10,10,-10,10])

#show and grilla
plt.grid()
plt.show()

