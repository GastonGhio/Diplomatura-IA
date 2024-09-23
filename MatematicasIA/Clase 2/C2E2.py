import sympy as sp
import numpy as np
from scipy.linalg import lu


A = np.array([[2,1,1],[4,-6,0],[-2,7,2]])
print(A)

P , L ,U = lu(A)

print("parte P")
print(P)
print("PARTE L")
print(L)
print("PARTE U")
print(U)
print("verificacion")

print(P@L@U)
# es identico qa hacer np.dot(P, np.dot(L,U))