
import pandas as pd

dst = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv")

dst_view = dst.loc[:,["anio", "mes"]] # los  "  :  " es similaer  * en SQL osea seleccionar todas las filas [[FILAS], [COLUMNAS]]

dst_view.shape

print(dst_view)

dst_view_sin_loc = dst[["anio", "mes"]]

print(dst_view_sin_loc)

#FUNCIONES DE GRUPO 

print(dst["anio"].sum())
print(dst["mes"].max())
print(dst["asignacion_por_cargo_i"].mean())
print(dst["total_salario_bruto_i_+_ii"].count())

print(dst[dst["reparticion"]== "SECR de Medios"]["total_salario_bruto_i_+_ii"].sum())
print(dst[dst["reparticion"]== "SECR Justicia y Seguridad"]["total_salario_bruto_i_+_ii"].sum())


print(dst["total_salario_bruto_i_+_ii"].max())
 
print(dst[dst["total_salario_bruto_i_+_ii"]== dst["total_salario_bruto_i_+_ii"].max()]) #le estoy pidiendo la columna entera

print(dst.describe().T)


