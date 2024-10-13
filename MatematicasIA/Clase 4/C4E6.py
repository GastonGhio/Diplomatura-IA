"""
Una persona tiene 40 metros de valla para construir un corral rectangular. Quieren maximizar el área del corral. ¿Cuáles deberían ser las dimensiones del corral? # Función a maximizar: Área del rectángulo (A = l * w) / considerar 1e6 # Normalizar para evitar desbordamiento, se utiliza el negativo para convertir la maximización en minimización
"""
from scipy.optimize import minimize


def area (x):
    l ,w = x
    return -1 * (l*w)

def restricciones(x):
    return 20 - (x[0]+ x[1])
    
bounds = [(0, None), (0,None)]

x0=[2,6] #suposicion

cons = {"type":"ineq", "fun":restricciones}

result=minimize(area, x0, method="SLSQP", bounds=bounds, constraints=cons)
print(result.x)

print(f"el area iootpima es de {-result.fun}")