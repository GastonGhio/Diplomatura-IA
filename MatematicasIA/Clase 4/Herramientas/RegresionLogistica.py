"""
Ejercicio 4: (como tarea) Se tiene un conjunto de datos que incluye el tiempo que un usuario pasa en un sitio web y si realiza o no una compra (1 si realiza una compra, 0 si no). La probabilidad de realizar una compra se modela con la función sigmoide (P(t) = \frac{1}{1 + e^{-mt}}), donde (t) es el tiempo en minutos y (m) es el parámetro a ajustar.

Objetivo: Encontrar el valor de (m) que maximiza la probabilidad de compra, es decir, que minimiza la función de pérdida asociada a la regresión logística.

Preguntas:

Define la función de pérdida para la regresión logística.
Utiliza métodos de optimización para encontrar el valor óptimo de (m).
"""

import numpy as np
from scipy.optimize import minimize

#datos de ejemplo ( tiempo en minutos y compras)
time_data = np.array([10,20,30,40,50])
purchase_data = np.array([0,0,1,1,1])

def logistic_loss(m):
    prediction = 1/(1+ np.exp(-m * time_data)) #es la prediccion de compra
    prediction = np.clip(prediction, 1e-15, 1 - 1e-15) # Ajusta las predicciones para evitar log(0) y log(1) npclip crea las limitaciones
    return -np.sum(purchase_data * np.log(prediction) + (1- purchase_data)* np.log(1- prediction)) 

# Encontrar el valor de m que minimiza la pérdida
optimal_m = minimize(logistic_loss, x0= [1], method="L-BFGS-B").x[0]
# Encuentra el valor óptimo de m mediante minimización
#`x0=[1]` establece el punto de partida para la búsqueda del mínimo de la función de pérdida,
#y `.x[0]` extrae el valor óptimo de \(m\) encontrado por el algoritmo de optimización.

print(f"Valor de m que maximiza la probabilidad de compra: {optimal_m}")