import sympy as sp

# LA RESOLVENTE

def factorizar_cuatrimestre(a, b, c):
    divisible = b**2 - (4*a*c)
    print(divisible)
    if divisible < 0 :
        return "no tiene raices reales"
    elif divisible == 0 :
        raizA=int(a**0.5)
        raizB=int(b**0.5)
        return f"{a}p^2 + {b}p + {c}= ({raizA}p + {raizB}p)^2"
    else:
        raiz1= (-b + divisible**0.5)/ (2*a)
        raiz2= (-b - divisible**0.5)/ (2*a)
        return f"las raices son {raiz1}, {raiz2}"
    
    
print(factorizar_cuatrimestre(-1,4,2))