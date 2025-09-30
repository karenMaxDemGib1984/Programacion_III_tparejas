#Importando la libreria y renombrandola a pd 
import pandas as pd
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

print("Primeras 5 filas de los datos:")
print(dataset.head())
print(" ")


print("Ultimas filas de los datos: ")
print(dataset.tail())
print(" ")

print("Datos ordenados por la columna 'A' (ascendente):")
print(dataset.sort_values(by='A').head())  # los primeros 5
print(" ")

print("Datos ordenados por la columna 'A' (descendente):")
print(dataset.sort_values(by='A', ascending=False).head())
print(" ")

# Seleccionar una columna (ejemplo con columna 'B')
columna = dataset['B']
print("Medidas estadísticas sobre la columna 'B':")
print("Media:", np.mean(columna))
print("Mediana:", np.median(columna))
print("Desviación estándar:", np.std(columna))