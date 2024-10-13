from scipy.optimize import minimize

def function(x):
    return x**2 - 6*x + 5


#definimios situacion inicial
x0=[0]
result=minimize(function, x0)

print(f" es el punto ddonde la funcion es minima, osea su minimizadcion{ result.x}")
print(result.fun)