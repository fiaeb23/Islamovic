# 1
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

import json
import requests
import os

def search_mealdb(query):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url, verify=False) #Zertifiaktabfrage deaktivieren
    
    if response.status_code == 200: #Status abfrage der http seite
        data = response.json()
        return data
    else:
        print("Fehler beim Abrufen der Daten.")
        return None

def get_all_meals():
   # all_meals=[]
    page = 1
    while True:
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s=&page={page}"
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            data = response.json()
            if data["meals"]:
                
                for meal in data["meals"]:
                    print("Name =", meal["strMeal"])
                page += 1 
                os.system("pause")
                menu()
                #komplette karte
                # all_meals.extend(data["meals"])
                # page += 1
                # print(data)
                # os.system("pause")
                # menu()

            else:
                break 
        else:
            print("Fehler beim Abrufen der Daten von MealDB.")
            return None


def save_results(data, filename="search_result.json"):
    #Dateiname als Pfad
    file_name = os.path.basename(filename)

    if data is not None:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=3)
            print(f"Die Suchergebnisse wurden in '{file_name}' gespeichert.")
    else:
        print("Die Daten sind ungültig, speichern nicht möglich.")

        # Datei erstellen, wenns nicht existiert
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump({}, json_file)
            print(f"Die Datei '{file_name}' wurde erstellt.")



def menu():
    while True:
        print("Menü:")
        print("1) Komplette Karte")
        print("2) Gericht suchen")
        print("3) Suchergebnis speichern")
        print("4) Beenden")
        choice = input("Bitte wählen Sie eine Option (1/2/3/4): ")

        if choice == '1':
            get_all_meals()

        elif choice == '2':
            query = input("Geben Sie den Suchbegriff ein: ")
            search_result = search_mealdb(query)

            if search_result:
                for elem in search_result["meals"]:
                    print("Name =", elem["strMeal"])

        elif choice == '3':
            if 'search_result' in locals():
                save_results(search_result)
            else:
                print("Keine Suchergebnisse zum Speichern vorhanden.")

        elif choice == '4':
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Eingabe (1/2/3/4).")

menu()
