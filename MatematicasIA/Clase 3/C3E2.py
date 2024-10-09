import sympy as sp

from scipy.integrate import quad


x = sp.symbols("x")

f = 1 / (1 + sp.exp(-x))

f_numerica =sp.lambdify(x, f)

a, b = 0 , 1 

#QUAD DEVUELVE VALOR Y SU ERROR
integral, error = quad(f_numerica,a,b)

print(f"la integraslde la {f}, es   {integral}, y su erorr es {error}")