from scipy.integrate import dblquad

#DEFINO LA FUNCION
def f(x, y ):
    return x + y 

#defino los limites
x_low, x_up = 0 , 1
y_low, y_up = 0,2

#pongo guion bajo porq no me importa el error
resultado, _ = dblquad(f, y_low, y_up, lambda y: x_low , lambda y: x_up)

print(resultado)