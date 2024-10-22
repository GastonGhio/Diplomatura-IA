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


print(casos)