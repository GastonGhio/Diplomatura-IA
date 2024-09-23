import numpy as np

A= np.array([[1,2],[3,4],[5,6]])

U , S ,VT = np.linalg.svd(A)

S_matris = np.zeros(A.shape)  # copia el modelo de la matriz pero con ceros

S_matris[:len(S), :len(S)] = np.diag(S)

A_reconstructed = U @ S_matris @ VT

print("Matriz A:")
print(A)
print("\n matriz U:")
print(U)
print("\nMatriz S (valores singulares):")
print(S_matris)
print("\nMatriz VT (transpuesta de la matriz de vectores singulares):")
print(VT)
print("\nVerificación: U * S * VT")
print(A_reconstructed)


