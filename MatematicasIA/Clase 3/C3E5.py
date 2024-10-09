import sympy as sp


#ESTAVBLESCO LAS VARIABLES
t = sp.symbols("t")

# ESTABLESCO F(X)
f = (t**2)*(1 / (1 + sp.exp(-t)))

#DERIVO 
derivada = sp.diff(f)

print(derivada)