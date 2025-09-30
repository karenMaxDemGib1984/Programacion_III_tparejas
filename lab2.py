#Importando la libreria y renombrandola a pd 
import pandas as pd

#Poniendo el dataset en una variable
dataset = pd.read_csv('data.csv')

#Salidas
print(dataset.head())
print(dataset.describe())
