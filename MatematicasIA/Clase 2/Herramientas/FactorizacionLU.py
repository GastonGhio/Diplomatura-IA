import sympy as sp
import numpy as np
from scipy.linalg import lu

A = np.array([[2,3,1],[4,7,5],[6,11,7]])

P, L ,U =lu(A)

print("Matriz A:")
print(A)
print("\nMatriz P (permutación):")
print(P)
print("\nMatriz L (triangular inferior):")
print(L)
print("\nMatriz U (triangular superior):")
print(U)
print("\nVerificación: P * L * U")
print(np.dot(P, np.dot(L, U)))