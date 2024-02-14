#Iván Ruipérez Benítez
import json
from funciones import menu,Opciones
with open("Data_Recipes.json") as fich:
    datos=json.load(fich)

num=0
while num != 6:
    num=menu()
    Opciones(num,datos)