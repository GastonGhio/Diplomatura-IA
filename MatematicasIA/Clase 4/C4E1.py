import sympy as sp

x= sp.symbols(" x ")

f= 20*x - 0.5*x**2
g= 200 + 3*x

u = f - g

print(u)

u_prima= sp.diff(u , x)
print(f"la funcion derivada de utilidades es {u_prima}")

#donde la derivada es 0 
critical_point = sp.solve(u_prima, x)
#para redondear a 1 decimal todo, tengo q hacer un ciclo dado q en la funcion puede haber muchos 0 osea formarse un arrya de numeros
# y por eso debo recorrerlo
critical_point_round = [ i.evalf(2) for i in critical_point]
print(f"los puntos criticos donde es 0 la derivada es {critical_point_round}")

u_prima2 = sp.diff(u_prima, x)
print(f"la segunda derivada es {u_prima2:.1f}")
if u_prima2 < 0 :
    print(f"eso quiere decir que {critical_point_round}, es un maximo")
else:
    print(f" eso quiere decir que {critical_point_round}, es un minimo")
    
ValorOptimo = critical_point_round[0]

profit = u.subs(x, ValorOptimo).evalf(2)

print(f" ganancia maxima en {ValorOptimo:.1f} da como resultado {profit}")