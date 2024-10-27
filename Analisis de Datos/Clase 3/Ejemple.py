import numpy as np
from scipy.integrate import quad
from mayavi import mlab

radius = 2.0
height = 5.0

def integrand(z):
    return np.pi*radius**2

result, error = quad(integrand, 0 , height)   #evalua entre 0 y 5

print("volumen calcuylado del cilibndro", result)
