'''
Parte 2: Carga de datos
Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:

Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
Calcular los promedios de las edades de cada dataset e imprimir.
'''

from datasets import load_dataset
import numpy as np
import pandas as pd
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
df = pd.DataFrame(data)
# Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
df_dead = df[df["is_dead"] == 1]
df_alive = df[df["is_dead"] == 0]
# Calcular los promedios de las edades de cada dataset e imprimir.
promedio_dead = df_dead["age"].mean()
promedio_alive = df_alive["age"].mean()
print(f"Promedios de personas que han muerto: {promedio_dead}")
print(f"Promedios de personas que siguen vivas: {promedio_alive}")






