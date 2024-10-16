import numpy as np
import pandas as pd

#leer base de datos publica

df = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv")

#COLUMS NOS TRAE TODAS LAS COLUMNAS
print(df.columns)

print(df.sample(5))

# SHAPE DEVUELVE (FILAS , COLUMNASS)

print(df.shape)

#SERIES PANDAS 
serie = pd.Series(["a", "b", "c", "d"])

print("tipos de objetos", serie.dtype)
print("nombre", serie.name)
print("index", serie.index)
print("valores", serie.values)


print("colunas", df.columns)
print("index", df.index)
print("dimensiones", df.shape)

#HEAD   muestra las primeras filas q pides
print(df.head(10))