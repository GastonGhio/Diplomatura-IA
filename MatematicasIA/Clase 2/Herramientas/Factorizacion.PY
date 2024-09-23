"""from sympy import symbols, factor

x, y = symbols("x y")
expr1 = 3 * x * y
fact1 = factor(expr1)
print(f"Factorización de monomio: {expr1} = {fact1}")"""

#DIFERENCIA DE CUADRFADOS
from sympy import symbols, factor, expand

x = symbols("x")

expr2= (x + 2)**2

fact2 = factor(expr2)

#REALIZA LA DISTRIBUTIVA CON EXPANDS
expand_factor= expand(fact2)

print(f"el ejercicio binomio cuadrfado {expr2}")
print(f" la factorizacion dio {fact2}")
print(f"el resultado dio {expand_factor}")

print("NOW WE MAKE THE EJERCISE THREE")

#FACTORIZACION POR AGRUPACION

expr3 = x**2 - 4 
fact3 = factor(expr3)

print(f"el factor es  {fact3}")

x, y, z, a = symbols ( " x y z a")

expr4= x*y + x*z + a*y + a*z

fact4 = factor(expr4)

print(f"el factor por agrupacion es {expr4} = {fact4}" )


# FACTOR COMUN
expr5= 3*x + 6*y
fact5 = factor(expr5)
print(f"el ejercicio 5, la expresion original es {expr5}, y factorizada por factor comunb es { fact5}")

#TRINOMIO  ax**2 + bx + c
expr6= x**2 + 3*x + 2
fact6 = factor(expr6)

print(f"el trimonio de la funcion {expr6}, es  {fact6}")