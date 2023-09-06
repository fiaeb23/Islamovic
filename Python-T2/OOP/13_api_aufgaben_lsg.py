import json
from urllib import request
import os
os.system("cls")

# url = "https://www.themealdb.com/api/json/v1/1/search.php?s=b"
# response = request.urlopen(url)
# data = json.load(response)

# for elem in data["meals"]:
#     print("Name =", elem["strMeal"])

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
"""
s = name
f = first letter
i = id
random.php = random

"""
#url = "https://www.themealdb.com/api/json/v1/1/search.php?s=Bigos"


url_main = "https://www.themealdb.com/api/json/v1/1/"

url_name = "search.php?s=" # Arrabiata
url_letter = "search.php?f=" # a
url_id = "lookup.php?i=" # 52772
url_ran = "random.php"

history = []
all_meals = {}


print("1) Durchsuchen der mealdb\n")
while True:
    os.system("cls")
    print("MealDB")
    print("Wonach möchtest du suchen?\n")
    print("Suche nach Namen [1]")
    print("Suche nach Anfangsbuchstaben [2]")
    print("Suche nach passender ID [3]")
    print("Zufälliges Gericht [4]")
    print("Beenden mit >x<")
    print()

    eingabe = input(">>> ")

    if eingabe == "1":

        while True:
            os.system("cls")
            print("Namenssuche:")
            print("Bitte Namen eingeben. Kann vollständig oder teilweise sein.")
            print("Bei keinen Ergebnissen bitte anders Beschreiben.")
            print("Beenden mit 0")
            print()

            eingabe_name = input(">>> ").replace(" ", "%20")
            history.append(eingabe_name)

            if eingabe_name == "0":
                os.system("cls")
                break

            else:
                url_final = url_main + url_name + eingabe_name
                response = request.urlopen(url_final)
                data = json.load(response)

                if data["meals"] == None:
                    print("Kein Fund!")
                else:
                    print("Deine Auswahl mit Namen:")
                    for elem in data["meals"]:
                        print("Name =", elem["strMeal"])


                with open(r"Aufgaben\history.json", "w") as file:
                    json.dump(history, file, indent=4)
                
                os.system("pause")

    elif eingabe == "2":

        while True:
            os.system("cls")
            print("Suche nach Buchstaben: ")
            print("Bitte nur ein einzelnen Buchstaben eingeben.")
            print("Bei keinen Ergebnissen bitte anders Beschreiben.")
            print("Beenden mit 0")
            print()

            eingabe_letter = input(">>> ").replace(" ", "%20")
            history.append(eingabe_letter)

            if eingabe_letter == "0":
                os.system("cls")
                break

            else:
                url_final = url_main + url_letter + eingabe_letter
                response = request.urlopen(url_final)
                data = json.load(response)

                if data["meals"] == None:
                    print("Kein Fund!")
                else:
                    print("Deine Auswahl mit Anfangsbuchstaben:")
                    for elem in data["meals"]:
                        print("Name =", elem["strMeal"])
                
                with open(r"Aufgaben\history.json", "w") as file:
                    json.dump(history, file, indent=4)

                os.system("pause")

    elif eingabe == "3":

        while True:
            os.system("cls")
            print("Suche nach ID: ")
            print("Bitte nur die korrekte ID eingeben.")
            print("Bei keinen Ergebnissen bitte anders Beschreiben.")
            print("Beenden mit 0")
            print()

            eingabe_id = input(">>> ").replace(" ", "%20")
            history.append(eingabe_id)

            if eingabe_id == "0":
                os.system("cls")
                break

            else:
                url_final = url_main + url_id + eingabe_id
                response = request.urlopen(url_final)
                data = json.load(response)

                if data["meals"] == None:
                    print("Kein Fund!")
                else:
                    print("Deine Auswahl mit ID: ")
                    for elem in data["meals"]:
                        print("Name =", elem["strMeal"])
                    
                with open(r"Aufgaben\history.json", "w") as file:
                    json.dump(history, file, indent=4)
                    
                os.system("pause")

    elif eingabe == "4":

        while True:
            os.system("cls")
            print("Zufälliges Gericht: ")
            print("Beenden mit 0")
            print()

            eingabe_ran = input("Eine beliebige Taste drücken...").replace(" ", "%20")
            history.append(eingabe_ran)

            if eingabe_ran == "0":
                os.system("cls")
                break

            else:
                url_final = url_main + url_ran + eingabe_ran
                response = request.urlopen(url_final)
                data = json.load(response)

                if data["meals"] == None:
                    print("Kein Fund!")
                else:
                    print("Deine Zufallsauswahl: ")
                    for elem in data["meals"]:
                        print("Name =", elem["strMeal"])
                        print()
                
                with open(r"Aufgaben\history.json", "w") as file:
                    json.dump(history, file, indent=4)
                    
                os.system("pause")

    elif eingabe == "x":
        print("Tschüss!")
        os.system("pause")
        os.system("cls")
        exit()

    elif eingabe == "all":

        url_all = "https://www.themealdb.com/api/json/v1/1/categories.php"
        response = request.urlopen(url_all)
        data = json.load(response)

        for elem in data["categories"][0]:
        #   print("Name =", elem["strMeal"])
            print("Kategorie =", elem["idCategory"])
            print("strCategory =", elem["strCategory"])
            print("strCategoryThumb =", elem["strCategoryThumb"])
            print("strCategoryDescription =", elem["strCategoryDescription"])
        
        print()
        os.system("pause")