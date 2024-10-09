from scipy.integrate import quad
import numpy as np
import sympy as sp

x = sp.symbols("x")

f = (x**2)



integral = sp.integrate(f,(x, 0 , 1))

print(integral)
