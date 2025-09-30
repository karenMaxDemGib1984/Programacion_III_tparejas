#Importando la libreria y renombrandola a pd 
import pandas as pd

#Poniendo el dataset en una variable
dataset = pd.read_csv('data.csv')

#Salidas
print("Resumen de los datos:")
print(dataset.describe())
print(" ")

print("Primeras 5 filas de los datos:")
print(dataset.head())
print(" ")


print("Ultimas filas de los datos: ")
print(dataset.tail())
print(" ")