import sympy as sp
from scipy.integrate import quad

#ESTAVBLESCO LAS VARIABLES
t = sp.symbols("t")

# ESTABLESCO F(X)
f = 1 / (1 + sp.exp(-t))

#DERIVO 
derivada = sp.diff(f)

print(derivada)