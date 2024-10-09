from scipy.integrate import tplquad
import plotly.graph_objects as go
import numpy as np

def f(x, y, z):
    return x**2 + y**2

a , b = 2 , 20
c, d = 0, 1
e, g = 0, 1

volumen, _ = tplquad(f, a, b, lambda x: c, lambda x: d, lambda x, y : e, lambda x, y: g)

print( volumen)


x = np.linspace(0,30,100)
y = np.linspace(0,30,100)
z = np.linspace(0,30,100)
x, y, z = np.meshgrid(x,y,z)

p=f(x,y,z)

fig = go.Figure(data=go.Volume(
    x=x.flatten(),  # Aplanar las matrices para que sean vectores
    y=y.flatten(),
    z=z.flatten(),
    value=p.flatten(),  # Los valores de la función en los puntos (x, y, z)
    isomin=np.min(p),  # Mínimo valor de la función a mostrar
    isomax=np.max(p),  # Máximo valor de la función
    opacity=0.5,  # Opacidad del volumen (transparencia)
    surface_count=15,  # Número de superficies dentro del volumen
    colorscale='Viridis',  # Escala de colores
    caps=dict(x_show=False, y_show=False, z_show=False)  # Ocultar las tapas de los ejes
))

fig.update_layout(
    title = "este es mi grafioco 3d",
    scene= dict(
        xaxis_title = "X",
        yaxis_title = "y",
        zaxis_title = "z",
    )
)

fig.show()

