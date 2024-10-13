from scipy.optimize import minimize_scalar

def function(x):
    return 3*x - 2

bounds= [-10, 10]
result=minimize_scalar(function, bounds=bounds, method="bounded")

print(f"valor optimo de x {result.x:.2f}")
print(f"el valor minimo de la funcion {result.fun:.2f}")