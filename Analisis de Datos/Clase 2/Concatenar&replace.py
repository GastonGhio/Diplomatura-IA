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

#concatenar PRIMER DEBEMOS IGUALAR LAWS TABLAS PARA EL JOIN

casos_panel["estado"] = "Confirmados"
casos_panel = casos_panel.rename(columns={
    "fecha_diagnostico": "fecha",
    "id_evento_caso": "casos"
})

print(casos_panel)

#MUCHA ATENCION HAY Q RENOMBRAR EL ESTADO  A MUERTO MORIDO EN LA SENTENCIA RENAME
casos_panel_muertos["estado"]="Morido"
casos_panel_muertos = casos_panel_muertos.rename(columns={
    "fecha_fallecimiento": "fecha",
    "id_evento_caso": "casos"
})
print(casos_panel_muertos)

casos_concat = pd.concat([casos_panel_muertos, casos_panel])
print(casos_concat)

# str PERMITE RENAME MAS DFACIL

casos_concat["sexo"] = casos_concat.sexo.str.replace(
    "F", "Femenino"
).replace(
    "M", "Masculino"
).replace(
    "NR", "No responde"
)
print(casos_concat.sexo.value_counts())