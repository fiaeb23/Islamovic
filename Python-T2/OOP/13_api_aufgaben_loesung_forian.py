import json
from urllib import request
import string

"""
https://www.themealdb.com/api.php

A) Entwickle ein Programm, mit welchem der Nutzer folgendes
   durchführen kann:
   1) Durchsuchen der mealdb
   2) Suchergebnisse speichern (in lokale json)
"""

# while True:
#     user_input = input("Gebe ein Gericht ein: ")
#     url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + user_input
#     response = request.urlopen(url)
#     data = json.load(response)

#     for elem in data["meals"]:
#         print("Name =", elem["strMeal"])
#     save_meal = input("Möchtest Du das Gericht speichern?")
#     if save_meal == "y":
#         file_name = input("Bitte gib der Datei einen Namen: ")
#         with open(file_name + ".json", "w", encoding="utf-8") as file:
#             json.dump(data, file, indent=4, ensure_ascii=False)


"""
BONUS)  
Überlege dir, wie du an ALLE daten der mealdb kommst
- speichere diese (im selben format) in eine lokale json
"""
letters = list(string.ascii_uppercase)

all_meals = {}
for letter in letters:
    url = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + letter
    response = request.urlopen(url)
    data = json.load(response)
    all_meals["meals_with_" + letter] = data["meals"]


with open("all_meals.json", "w", encoding="utf-8") as file:
    json.dump(all_meals, file, indent=4, ensure_ascii=False)
    print("Gespeichert!")

"""
#for key, value in data["meals"][0].items():
#    print(f"{key} ({type(value)}):", value)

for i in range(1, 21):
    if data["meals"][0]["strIngredient"+str(i)]:
        print(data["meals"][0]["strIngredient"+str(i)], "-", data["meals"][0]["strMeasure"+str(i)])
        #"digestive biscuits - 175g/6oz"
"""
