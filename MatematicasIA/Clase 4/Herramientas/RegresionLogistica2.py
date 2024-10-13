import sympy as sp
import numpy as np
from scipy.optimize import minimize

a, m = sp.symbols("a m")
sigmoid_function= 1 / (1 + sp.exp(-m*a))

profit_per_sale= 100
loss_incorrect_prediction= 50

def ganancias (m):
    prediction = 1 /(1+ np.exp(-m * customer_atribute))
    # hago el ajuste de la prediccion
    prediction = np.clip(prediction, 1e-15 , 1- 1e-15)
    expected_purchases= np.sum(prediction)
    expected_prediction_incorrect = len(customer_atribute) - expected_purchases
    
    net_profit = expected_purchases*profit_per_sale - expected_prediction_incorrect * loss_incorrect_prediction
    return  -net_profit #el negatuicvo es para volverlo maximizacion y no minimizacion

customer_atribute= np.array([0.5, 0.7, 0.3, 0.9, 0.6])

# esta linea no recuerdo porq se utilizaba
optimal_m= minimize(ganancias, x0=[1], method="L-BFGS-B").x[0]

# Mostrar resultado
print("\nEjercicio 5: Ajuste de Modelo para Maximizar Ganancias")
print(f"Valor óptimo de m que maximiza las ganancias: {optimal_m:.2f}")