import sympy as sp

x , y= sp.symbols("x y")

f = 1 / (1 + sp.exp(-x))

# le paso la funcion dsp la varuiable de cual derivar
derivada = sp.diff(f, x)
derivada2 = sp.diff(x**2, x)
derivada3 = sp.diff(f, y)

print(derivada)
print(derivada2)
print(derivada3)