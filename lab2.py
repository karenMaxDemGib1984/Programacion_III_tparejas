#Importando la libreria y renombrandola a pd 
import pandas as pd
#Importando la libreria numpy y renombrandola a np
import numpy as np

#Poniendo el dataset en una variable
dataset = pd.read_csv('data.csv')

#Salidas
print("Resumen de los datos:")
print(dataset.describe())
print(" ")

# Identificar tipos de datos
print("Tipos de datos en cada columna:")
print(dataset.dtypes)
print(" ")

#Salida de las primeras 5 filas
print("Primeras 5 filas de los datos:")
print(dataset.head())
print(" ")

#Salida de las ultimas 5 filas
print("Ultimas filas de los datos: ")
print(dataset.tail())
print(" ")

#Ordenando el dataset con la columna A de manera ascendente
print("Datos ordenados por la columna 'A' (ascendente):")
print(dataset.sort_values(by='A').head())  # los primeros 5
print(" ")

#Ordenando el dataset con la columna A de manera descendente
print("Datos ordenados por la columna 'A' (descendente):")
print(dataset.sort_values(by='A', ascending=False).head())
print(" ")

# Seleccionar una columna (ejemplo con columna 'B')
columna = dataset['B']
print("Medidas estadísticas sobre la columna 'B':")
print("Media:", np.mean(columna))
print("Mediana:", np.median(columna))
print("Desviación estándar:", np.std(columna))