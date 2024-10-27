import numpy as np
from mayavi import mlab


x, y, z = np.mgrid[-5:5:0.1, -5:5:0.1, -5:5:0.1] #crea matriz 
values = np.sin(np.sqrt(x**2 + y**2 + z**2)) #calcula los valores de la funcion tridimensioanl

plot = mlab.figure(size =(800,600), bgcolor =(1,1,1), fgcolor=(0,0,0))

mlab.contour3d(x,y,z, values, colormap="viridis")

#ajustar la vista
mlab.view(azimuth=45, elevation=60, distance=10) #azimuth es el angulo horinzontal

mlab.show()