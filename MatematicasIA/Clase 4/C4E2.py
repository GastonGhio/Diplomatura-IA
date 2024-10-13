import sympy as sp


x = sp.symbols("x")

r = 15*x - 0.2*x**2


r_prima= sp.diff(r, x)
print(r_prima)

critical_points= sp.solve(r_prima, x)
print(f"los puntos criticos sin rangfo son {critical_points}")

critical_points_range= [i.evalf(3) for i in critical_points if i >= 0 and i <= 100]
print(f"los puntos criticos son redondeados sin coma son  {critical_points_range}")

r_prima2 = sp.diff(r_prima, x)

print (f"la pendiente es {r_prima2}")

for i in critical_points_range:
    if r_prima2.subs(x, i) > 0:
        print(f"El punto {i} es un mínimo (minimiza los costos).")
    elif r_prima2.subs(x, i) < 0:
        print(f"El punto {i} es un máximo (maximiza los ingresos).")