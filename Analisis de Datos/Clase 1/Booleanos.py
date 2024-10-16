import numpy as np
import pandas as pd

df = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv")

print(df.columns)
mask_boolean = print(df["anio"] != 2019)

#muchas formas de llamar, [n,m..], valor unico, condicion boobleana, slice de columnas ["nombre": "direccion"]
ministerioCultura = df.loc[df["reparticion"] == "Ministerio de Cultura", :]

print(ministerioCultura)

query1 =df[(df["total_salario_bruto_i_+_ii"] > 240000) | (df["aguinaldo_ii"] > 0)]

print(query1)

query2 = df[(df["mes"] == 2) & (df ["reparticion"] == "SECR Ciencia, Tecnologia e Innovacion")]

print("esta es la busqueda de mes febrero y de la reparticion de ciencia y tecnologia ", query2)


