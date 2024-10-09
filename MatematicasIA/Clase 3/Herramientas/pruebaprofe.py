from bokeh.plotting import figure, show, output_notebook
from bokeh.plotting import output_file

# Genera la salida en un archivo HTML en lugar de en el notebook
output_file("sigmoid_plot.html")

# Activa la salida de Bokeh en el notebook
output_notebook()

# Ejemplo simple de Bokeh
p = figure(title="Ejemplo simple", x_axis_label='x', y_axis_label='y')
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Linea simple", line_width=2)

show(p)