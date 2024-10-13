"""_
    
La función minimize y la función minimize_scalar son parte del paquete scipy.optimize, pero tienen diferentes propósitos y aplicaciones.

minimize: Esta función se utiliza para minimizar una función de varias variables (es decir, una función que toma varios valores como entrada y devuelve un solo valor como salida). Puede manejar problemas de optimización multidimensionales y ofrece una variedad de algoritmos de optimización que se adaptan a diferentes tipos de funciones y restricciones.

minimize_scalar: Esta función, como su nombre indica, se utiliza para minimizar una función de una sola variable (es decir, una función que toma un solo valor como entrada y devuelve un solo valor como salida). Está diseñada específicamente para problemas de optimización unidimensionales y utiliza métodos que son eficientes para este tipo de problemas. por ejemplo calculos de funciones cuadraticas, exponenciales y/o lineales
"""
    
from scipy.optimize import minimize_scalar

def function_cuadratic(x):
    return x**2 - 6*x + 5

resultado= minimize_scalar(function_cuadratic)

# punto x es solo para q imprima x y no toda la informacion
print(resultado.x)