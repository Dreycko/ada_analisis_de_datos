''' 

Una vez cargado el csv mediante el request anterior, realiza lo siguiente:

Verificar que no existan valores faltantes
Verificar que no existan filas repetidas
Verificar si existen valores atípicos y eliminarlos
Crear una columna que categorice por edades
0-12: Niño
13-19: Adolescente
20-39: Jóvenes adulto
40-59: Adulto
60-...: Adulto mayor
Guardar el resultado como csv
Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.
'''

import pandas as pd
import numpy as np

def ej_4_procesar_datos(df: pd.DataFrame) -> pd.DataFrame:
    # Verificar que no existan valores faltantes
    print(df.isnull().sum())
    # Verificar que no existan filas repetidas
    print(df.duplicated().sum())
    # Verificar si existen valores atípicos y eliminarlos
    # Calcular los cuartiles
    q1 = df["age"].quantile(0.25)
    q3 = df["age"].quantile(0.75)
    # Calcular el rango intercuartil
    iqr = q3 - q1
    # Eliminar los outliers
    df = df[(df["age"] >= q1 - 1.5 * iqr) & (df["age"] <= q3 + 1.5 * iqr)]
    # Crear una columna que categorice por edades
    # 0-12: Niño
    # 13-19: Adolescente
    # 20-39: Jóvenes adulto
    # 40-59: Adulto
    # 60-...: Adulto mayor
    df["age_category"] = np.where(df["age"] <= 12, "Niño", np.where(df["age"] <= 19, "Adolescente", np.where(df["age"] <= 39, "Joven adulto", np.where(df["age"] <= 59, "Adulto", "Adulto mayor"))))
    # Guardar el resultado como csv
    df.to_csv("clean_heart_failure_clinical_records_dataset.csv", index=False)
    return df

# se lee el archivo csv
df = pd.read_csv("heart_failure_clinical_records_dataset.csv")
# se llama a la funcion
ej_4_procesar_datos(df)

