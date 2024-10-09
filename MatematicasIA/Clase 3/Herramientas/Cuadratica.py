#@title Imports

import numpy as np
import scipy.optimize as opt  # import root-finding algorithm
import sympy as sp  # Python toolbox for symbolic maths
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Toolbox for rendring 3D figures
from mpl_toolkits import mplot3d  # Toolbox for rendring 3D figures

#genera datos para la f cudratica
xs = np.linspace(-2.1 , 2.1 , 500)
ys = xs**2 

#creamos graficos
plt.plot(xs,ys)

# Agregar una línea vertical en x=0 y una línea horizontal en y=3
plt.plot([0,0],[0,3], "k--") # "k--" representa una línea negra punteada

plt.arrow(-1.4, 2.5, 0.5,-1.3, head_width=0.1, color="b")

plt.arrow(0.85, 1.05, 0.5, 1.3 , head_width=0.1, color="b")

plt.show()