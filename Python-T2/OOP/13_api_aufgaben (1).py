import json
from urllib import request

url = "https://www.themealdb.com/api/json/v1/1/search.php?s=b"
response = request.urlopen(url)
data = json.load(response)

for elem in data["meals"]:
    print("Name =", elem["strMeal"])

"""
https://www.themealdb.com/api.php

A) Entwickle ein Programm, mit welchem der Nutzer folgendes
   durchführen kann:
   1) Durchsuchen der mealdb
   2) Suchergebnisse speichern (in lokale json)

BONUS)  
Überlege dir, wie du an ALLE daten der mealdb kommst
- speichere diese (im selben format) in eine lokale json
"""



"""
#for key, value in data["meals"][0].items():
#    print(f"{key} ({type(value)}):", value)

for i in range(1, 21):
    if data["meals"][0]["strIngredient"+str(i)]:
        print(data["meals"][0]["strIngredient"+str(i)], "-", data["meals"][0]["strMeasure"+str(i)])
        #"digestive biscuits - 175g/6oz"
"""