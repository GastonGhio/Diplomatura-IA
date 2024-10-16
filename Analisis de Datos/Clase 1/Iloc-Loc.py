import numpy as np
import pandas as pd

df = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv")


# ILOC[columnas, filas]   esa es su estructura BASADO EN NPOSICION
#muchas formas de llamar, [n,m..], valor unico
print(df.iloc[3:5 , 3:5])


#muchas formas de llamar, [n,m..], valor unico, condicion boobleana, slice de columnas ["nombre": "direccion"]
# SE BASA EN EL NOMBRE DE LAS COLUMNAS
print(df.loc[df["funcionario_nombre"] == "Horacio", :])

print(df.columns)
