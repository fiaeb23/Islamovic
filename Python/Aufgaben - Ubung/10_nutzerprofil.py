# """
# Erstelle ein CLI-Tool mit dem sich ein Nutzerprofil darstellen lässt

# Hole zunächst folgende Informationen vom Nutzer:
# 1) Name
#    - Ein Name muss aus mind. 3 Zeichen bestehen
#    - Ein Name darf keine Zahlen enthalten
# 2) Geburtsjahr
#    - Es muss ein valides und "realistisches" Geburtsjahr sein
#    - Das Mindestalter zur Nutzung des Programms ist 18
# 3) Wohnort
#    - Ein Wohnort muss aus mind. 5 Zeichen bestehen
#    - Ein Wohnort darf keine Zahlen enthalten
   
# Anschließend kann der Nutzer über ein Menü:
# - Seinen Namen verändern
#   (beachte die Namens-Regeln!)
# - Sein Geburtsjahr verändern
#   (beachte die Geburtsjahr-Regeln!)
# - Seinen Wohnort verändern
#   (beachte die Wohnort-Regeln!)
# - Programm beenden

# Tipp: Verwende die len()-Funktion
# """


import datetime


# Hauptfunktion des Programms
def main():
    name = get_name()
    birthyear = get_birthyear()
    location = get_location()
    print(f"Dein Nutzerprofil: Name: {name}, Geburtsjahr: {birthyear}, Wohnort: {location}")
    
    while True:
        print("\nWas möchtest du ändern?")
        print("[1] Name")
        print("[2] Geburtsjahr")
        print("[3] Wohnort")
        print("[4] Beenden")
        
        choice = input("Gib deine Auswahl ein (1-4): ")
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Ungültige Auswahl! Gib deine Auswahl ein (1-4): ")
        
        if choice == "1":
            name = get_name()
        elif choice == "2":
            birthyear = get_birthyear()
        elif choice == "3":
            location = get_location()
        else:
            break
    
    print(f"Dein neues Nutzerprofil: Name: {name}, Geburtsjahr: {birthyear}, Wohnort: {location}")
    


# Funktion zum Überprüfen, ob ein String nur aus Buchstaben besteht
def only_letters(string):
    return all(char.isalpha() for char in string)


# Funktion zum Überprüfen, ob ein String nur aus Zahlen besteht
def only_numbers(string):
    return all(char.isdigit() for char in string)


# Funktion zum Einlesen des Namens
def get_name():
    name = input("Gib deinen Namen ein: ")
    while len(name) < 3 or not only_letters(name):
        print("Ungültiger Name! Der Name muss aus mind. 3 Buchstaben bestehen und darf keine Zahlen enthalten.")
        name = input("Gib deinen Namen ein: ")
    return name


# Funktion zum Einlesen des Geburtsjahrs
def get_birthyear():
    birthyear = input("Gib dein Geburtsjahr ein (xxxx): ")
    while not only_numbers(birthyear) or int(birthyear) > datetime.datetime.now().year - 18:
        print("Ungültiges Geburtsjahr! Das Geburtsjahr muss ein valides und 'realistisches' Jahr sein und du musst mindestens 18 Jahre alt sein.")
        birthyear = input("Gib dein Geburtsjahr ein (xxxx): ")
    return birthyear


# Funktion zum Einlesen des Wohnorts
def get_location():
    location = input("Gib deinen Wohnort ein: ")
    while len(location) < 3 or not only_letters(location):
        print("Ungültiger Wohnort! Der Wohnort muss aus mind. 5 Buchstaben bestehen und darf keine Zahlen enthalten.")
        location = input("Gib deinen Wohnort ein: ")
    return location



if __name__ == "__main__":
    main()
