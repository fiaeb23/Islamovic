import json
from urllib import request

url = "https://www.themealdb.com/api/json/v1/1/categories.php"
response = request.urlopen(url)
data = json.load(response)

all_meals = []
for category in data["categories"]:
    strCategory = category["strCategory"]
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + strCategory
    response = request.urlopen(url)
    category_data = json.load(response)   
    #print(len(category_data["meals"]))
    all_meals.extend(category_data["meals"])

  
print(len(all_meals))

with open(r"Desktop\all_meals.json", "w", encoding="utf-8") as file:
    json.dump(all_meals, file, indent=4)

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