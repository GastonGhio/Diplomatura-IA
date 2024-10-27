import numpy as np
import plotly.graph_objects as go

np.random.seed(42)

points= 100
x = np.random.rand(points)
y = np.random.rand(points)
z = np.random.rand(points)

plot = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode = "markers", marker=dict(color="red", size=7))])

plot.update_layout(scene=dict(xaxis_title="'X Label'", yaxis_title="'Y Label'", zaxis_title="'Z Label'"),
                   title="scatter plot 3d - plotly")



"""plot.write_html("prueba html plotly")"""
open("prueba html plotly")