import sympy as sp

x, y = sp.symbols("x y ")

f = (x*y)**2 + ( 1 / (1 + sp.exp(-x)))

derivadaX= sp.diff(f, x)
derivadaY= sp.diff(f, y)

print(f"la d3erivbada parcuial de {f}, es  {derivadaX} + {derivadaY}")