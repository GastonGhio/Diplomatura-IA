import pandas as pd

dataSet = pd.read_csv("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv")

query1 = dataSet.query("reparticion == 'Ministerio de Cultura'")  

print(query1)

query2 = dataSet.query("asignacion_por_cargo_i > 240000 & aguinaldo_ii > 0")

print("esto es querry2", query2)

query2.shape

#AMVBOS METODOS .QUERY O [] SON IGUALES, .QUERY ES SIMILAR A SQL Y MAS LEGIBLE, [] PERMITE BUSQUEDAS MAS COMPLEJAS Y .LOC .ILOC

data = dataSet[dataSet["mes"] > 10]
print(data)

query3 = dataSet.query("mes > 10")
print(query3)