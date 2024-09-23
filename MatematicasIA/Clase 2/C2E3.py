import numpy as np

A= np.array([[1,3,5],[2,4,6]])

U , S, VT = np.linalg.svd(A)

matrizB = np.zeros(A.shape) # crea una copia de la matriz
print(matrizB)

matrizB[:len(S), :len(S)] = np.diag(S)
print(matrizB)

reconstruccion = U@matrizB@VT

print("Matriz A:")
print(A)
print("\nMatriz U:")
print(U)
print("\nMatriz S (valores singulares):")
print(matrizB)
print("\nMatriz VT (transpuesta de la matriz de vectores singulares):")
print(VT)
print("\nVerificación: U * S * VT")
print(reconstruccion)