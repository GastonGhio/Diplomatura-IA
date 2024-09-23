from sympy import symbols, factor, collect

"""
 ¿Cuándo usar collect()?
Para reorganizar ecuaciones: Si tienes una expresión complicada con varias variables y quieres agrupar términos en función de una o más variables específicas.
Al resolver ecuaciones: Puede ser útil para simplificar ecuaciones antes de resolverlas.
Polinomios: Cuando trabajas con polinomios y deseas ver cómo se distribuyen los términos según las potencias de una variable.
"""

#FACTOR COMUN 
u, v, w = symbols("u v w")

expr1= 2*u*v + 3*u*w + - 4*v*w

fact1 = collect(expr1, u)

print(f"la escuacion {expr1}, agrupada por collect es {fact1}")

fact2= collect(expr1, v)

print(f"la escuacion {expr1}, agrupada por collect es {fact2}")


#DIVISION SINTETICA
x, y = symbols("x y ")


expr3 = x**3 - 6*x**2 + 11*x - 6
fact3= factor(expr3)
print(f"la diviosn del polinomio {expr3}, es  {fact3}")


