import numpy as np

A = np.array([[4,-2],[1,1]])

#descomposicion eig de numpy
# esta funcion devuelve 2 objetos 
eigenvalues , eigenvectors = np.linalg.eig(A)

print("matriz A")
print (A)

print("\n valores propios")
print(eigenvalues)

print("\n vectores propios")
print(eigenvectors)


# Verificación de la descomposición
# A debería ser igual a V * D * V^{-1}
# np.allclose verifica si dos matrices son iguales (dentro de una tolerancia numérica)
# np.diag(eigenvalues) crea una matriz diagonal a partir del array de valores propios
# np.linalg.inv(eigenvectors) calcula la inversa de la matriz de vectores propios
print("\nVerificación: A = V * diag(D) * inv(V)")
print(np.allclose(A, eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)))