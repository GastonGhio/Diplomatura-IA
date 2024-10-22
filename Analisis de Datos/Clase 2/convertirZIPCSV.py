import zipfile
from io import BytesIO
import pandas as pd

# escribimos la direcion del zuip

zip_ubication = r"C:\Users\Biogh\Downloads\covid_casos (1).zip"

#leer el archivo zip
with zipfile.ZipFile(zip_ubication, "r") as zip_trasnformado:
    #seleccionamos el primer archivo en el zip (depenmde tu estructura)
    csv_file = zip_trasnformado.namelist()[0]
    
    #lee el csv dentro del zip
    with zip_trasnformado.open(csv_file) as csv_transcision:
        
        # utiliza bytesio para convertir el contenido en un formato pandas
        csv_convertido = BytesIO ( csv_transcision.read())
        
        casos = pd.read_csv(csv_convertido)


print(casos.head())

print(casos.columns)

print(casos.residencia_provincia_nombre.unique())

print("estas son las columnas q inician con fecha")
for col in casos.columns:
    if col.startswith("fecha"):
        
        print(col)
        
        
casos_confirm=casos[casos.clasificacion_resumen == "Confirmado"].pivot_table(
    index = ["residencia_provincia_nombre"],
    values=["id_evento_caso"],
    aggfunc="count"
)
print(casos_confirm.sort_values("id_evento_caso", ascending=True))

"""tilizas la función pivot_table de pandas para crear una tabla dinámica (pivot table) que agrupa los datos por residencia_provincia_nombre, y cuentas el número de casos (id_evento_caso) para cada provincia.
"""

print("la cantidad de casos conrfirmado  en todo el pais es de  ",casos_confirm.id_evento_caso.sum())

casos_muertes = casos[casos["fecha_fallecimiento"].notnull()]

tabla_muertes = casos_muertes["id_evento_caso"].count()

print("la tabla de fallidos es:")

print(tabla_muertes)

casos_panel = casos[casos.clasificacion_resumen == "Confirmado"].pivot_table(
    index=[
        "residencia_provincia_id",
        "residencia_provincia_nombre",
        "sexo",
        "fecha_diagnostico"
    ],
    values=["id_evento_caso"],
    aggfunc="count"
).reset_index()

print(casos_panel.head(100))


casos_panel_muertos = casos[casos.clasificacion_resumen == "Confirmado"].pivot_table(
    index=[
        "residencia_provincia_id",
        "residencia_provincia_nombre",
        "sexo",
        "fecha_fallecimiento"
    ],
    values=["id_evento_caso"],
    aggfunc="count"
).reset_index()

print(casos_panel_muertos.head(100))