from scipy.integrate import dblquad
import plotly.graph_objects as go
import numpy as np

def f(x, y):
    return x**5 + y**5 + x 

a , b = 0 , 1
c, d = 0, 1


volumen, _ = dblquad(f, a, b, lambda x: c, lambda x: d)

print( volumen)


x = np.linspace(0,3000,100)
y = np.linspace(0,3000,100)
z = np.linspace(0,30,100)
x, y = np.meshgrid(x,y)

z=f(x,y)
fig = go.Figure(data=go.Surface(z=z, x=x, y=y))


fig.update_layout(
    title = "este es mi grafioco 3d",
    scene= dict(
        xaxis_title = "X",
        yaxis_title = "y",
        zaxis_title = "z",
    )
)

fig.show()
