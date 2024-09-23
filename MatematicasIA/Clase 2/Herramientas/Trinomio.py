import sympy as sp

def resolvente (a, b, c):
    divisor = b**2 - 4 * a*c
    if divisor < 0:
        return "no le tiene raices"
    raiz1=( b + divisor ** 0.5) / (2 *a)
    raiz2 =( -b + divisor ** 0.5 )/ (2 *a)
    return f"{a}x^2 + {b}x + {c} = (x- {int(raiz1)}) * (x - {int(raiz2)})"

print(resolvente (1 , -5 , 6))


def sumaCubos (a,b):
    formula = a**3 + b**3
    return  f"{a}^3 + {b}^3 = ({a} + {b})({a**2} - {a*b} + {b**2})"

numero1 = 1
numero2 = 3

print(sumaCubos(numero1,numero2))

def factorizarDifcub():
    y =sp.symbols("y")
    expr = y **3 - 64
    factorizada = sp.factor(expr)
    return expr, factorizada

original, factorizada = factorizarDifcub()
print(f"la original es {original}")
print(f" la factorizada es {factorizada}")