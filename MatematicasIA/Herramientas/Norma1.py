#calculo de la NORMA raiz (todo elevevado al cuadrado)
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA 

def plotVector (vector, origin=[0,0], **option):
    
    return plt.arrow(origin[0], origin[1], vector[0], vector[1], head_width=0.5, head_length = 0.4, length_includes_head=True, **option)

u = np.array([6, 5])
v = np.array([8, 1])

print(LA.norm(u))

w = np.array([4, 2])
print(" ", u)
print("+", v)
print("+", w)
print("-"*10)
print(u + v + w)

plotVector(u, color="r")
plotVector(v, color="blue")
plotVector(u+v, color="g")

# Añadimos texto "u" en la posición (0.7, 3) en color rojo y tamaño de fuente 18.
plt.text(1.5, 3, "vector u", color="r", fontsize=8)
plt.text(5,2, "vector u + v",color="g", fontsize=8)
plt.text(8,0.6, "vector v",color="b", fontsize=8)


plotVector(u, origin=v, color="gray", linestyle= "dotted")
plotVector(v, origin=u, color="gray", linestyle= "dotted")



 #traza los limites del eje X y el Y
plt.axis([0,20,0,12])

#show and grilla
plt.grid()
plt.show()
