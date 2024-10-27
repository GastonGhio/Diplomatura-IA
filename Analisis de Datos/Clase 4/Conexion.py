#diferentes formas de conectarse a base de datos con distintos programas

import sqlite3

#conn= sqlite3.connect("_memory:")


import mysql.connector

conn1= mysql.connector.connect(
    
)

import pandas as pd
import numpy as np

# Cargar datos de calidad del vino
df_vino = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')
print(df_vino.columns)


# donde hay valores nulos tira nan
data = {
    "A": [1,2,np.nan,4,5],
    "B": [np.nan,2,3,4,5],
    "C": [1,2,3,4,np.nan],
    "D": [1,np.nan,3,np.nan,5]
}

ejemplo = pd.DataFrame(data)

print(data)

print("estos son los valores nulos del computo")

#me dice la cantidad 
print(ejemplo.isnull().sum())


interpolacion = ejemplo.interpolate()

print(interpolacion)