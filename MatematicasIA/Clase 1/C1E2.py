import matplotlib.pyplot as plt
import numpy as np

def desplazar_puntos(a,b,c,d):
    desplaz= np.array([7,5])
    a_ = a + desplaz
    b_ = b + desplaz
    c_ = c + desplaz
    d_ = d + desplaz
    #return a_,b_,c_,d_
    
a = np.array([1,1])
b = np.array([1,2])
c = np.array([2,3])
d = np.array([8,4])

x_coords, y_coords = zip(a,b,c,d,a)
plt.plot(x_coords, y_coords, "c--", x_coords, y_coords, "co")

a_,b_,c_,d_ = desplazar_puntos(a,b,c,d)
x_coords_b, y_coords_b = zip(a_,b_,c_,d_,a_)
plt.plot(x_coords_b, y_coords_b, "b-", x_coords_b, y_coords_b, "bo")

plt.show()