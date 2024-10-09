import sympy as sp

x, y , z = sp.symbols("x y z")
f = x + y + z

int1= sp.integrate(f, (x ,0 , 1))

int2 = sp.integrate(int1 , (y ,0,1))

int3= sp.integrate(int2,( z, 0 ,1))

print(f"el resultado final es {int3}")

