from sympy import symbols, factor, expand

x = symbols("x")
expr = x**2 + 14*x + 49
fact = factor(expr)

print(f"la expresion {expr} == {fact}")