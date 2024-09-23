from sympy import symbols, factor 

m = symbols("m")

expr= m**2 + 6*m + 9
fact = factor(expr)

print(fact)

y = symbols("y")
expr2=y**2 - 10*y + 25
fact2= factor(expr2)

print(fact2)

a= symbols("a")
expr3= a**2 - 8*a + 16
fact3=factor(expr3)

print(fact3)