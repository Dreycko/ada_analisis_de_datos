'''
Parte 3: Calculando analíticas simples
Continuando con el DataFrame con todos los datos de la anterior subsección, ahora debes:

Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).
'''

from datasets import load_dataset
import numpy as np
import pandas as pd
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
# Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
df = pd.DataFrame(data)
# Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
print(df.dtypes)
# Calcular la cantidad de hombres fumadores (usando agregaciones en Pandas).
df_smoker = df[df["is_smoker"] == 1]
# is_male = 1
df_smoker_hombre =  df_smoker[df_smoker["is_male"] == 1]
df_smoker_mujer = df_smoker[df_smoker["is_male"] == 0]
print(f"Hombres: {len(df_smoker_hombre)}")
print(f"Mujeres: {len(df_smoker_mujer)}")
















