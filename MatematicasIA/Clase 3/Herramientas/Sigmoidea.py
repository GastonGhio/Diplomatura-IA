import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.models import HoverTool, ColumnDataSource

# Activa la salida de Bokeh en el notebook
output_notebook()
output_file("sigmoide.html")

# Definición de la función sigmoidal
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoidal
def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# Definimos el rango de valores para x
x = np.linspace(-10, 10, 400)

# Calculamos la función sigmoide y su derivada
y = sigmoid(x)
y_derivada = sigmoid_derivative(x)

# Creamos el DataFrame
data = pd.DataFrame({
    "x": x,
    "sigmoid": y,
    "sigmoid_derivative": y_derivada
})

# Convertimos el DataFrame a un ColumnDataSource
source = ColumnDataSource(data)

# Creamos el gráfico
p = figure(title="Función sigmoide y su derivada",
           x_axis_label="x", y_axis_label="y",
           width=800, height=400)

# Agregamos la función sigmoidal usando ColumnDataSource
p.line('x', 'sigmoid', source=source, legend_label="Sigmoid Function", line_width=2)

# Agregamos la derivada de la función sigmoidal
p.line('x', 'sigmoid_derivative', source=source, legend_label="Sigmoid Derivative", line_width=2, line_dash='dashed', color='orange')

# Agregamos las herramientas de hover con referencia al ColumnDataSource
hover = HoverTool()
hover.tooltips = [("x", "@x"), ("Sigmoid", "@sigmoid"), ("Sigmoid Derivative", "@sigmoid_derivative")]
p.add_tools(hover)

# Mostramos el gráfico
show(p)