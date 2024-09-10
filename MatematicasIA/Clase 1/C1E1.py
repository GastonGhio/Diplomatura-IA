import numpy as np

u = np.array([1, 0])
v = np.array([5, 1])
def son_ortogonales(u,v):
    esOrtogonal = np.dot(u,v) 
    if esOrtogonal == 0:
        print("es ortogonal la cosa")
    else:
        print("no es ortogonal")
        
son_ortogonales(u, v)