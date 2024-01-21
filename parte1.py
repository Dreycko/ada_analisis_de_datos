'''
Al indexar por una característica, obtenemos una lista con los valores de todos los registros para esa colúmna.
Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio.
'''
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

import numpy as np
edades = np.array(data["age"])
promedio = edades.mean()
print(promedio)




