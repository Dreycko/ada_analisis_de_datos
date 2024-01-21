'''Parte 4: Procesando información en bruto
Imagina que no tuvieramos el acceso fácil de estos datos a través de la librería y tuvieramos que descargar los datos usando requests.

Los datos son accesibles en esta dirección: https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv

Realiza un GET request para descargarlos y escribe la respuesta como un archivo de texto plano con extensión csv (no necesitas pandas para esto, sólo manipulación de archivos nativa de Python)
Agrupa el código para esto en una función reutilizable que reciba como argumento la url.'''

import requests
import pandas as pd


def ej_4_descargar_datos(url: str) -> None:
    # Realiza un GET request para descargarlos y escribe la respuesta como un archivo de texto plano con extensión csv (no necesitas pandas para esto, sólo manipulación de archivos nativa de Python)
    response = requests.get(url)
    # se guarda el archivo en la carpeta data
    with open('./heart_failure_clinical_records_dataset.csv', 'w') as f:
        f.write(response.text)
    # se lee el archivo csv
    df = pd.read_csv('./heart_failure_clinical_records_dataset.csv')
    # se guarda el DataFrame en un archivo csv
    df.to_csv('./heart_failure_clinical_records_dataset.csv', index=False)
    
   
# se llama a la funcion
ej_4_descargar_datos('https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv')

