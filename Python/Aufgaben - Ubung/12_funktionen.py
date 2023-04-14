import os

user_name = "Klaus"

def hallo_sagen(menu_name):
    print("Hallo", user_name)
    print("Du befindest dich im", menu_name)
    
def addieren(x, y):
    return x + y


while True:
    os.system("cls")
    hallo_sagen("Hauptmenü")
    print("[1] Zahlen addieren")
    print("[2] Untermenü B")
    print("[x] Beenden")
    eingabe = input(">>> ")
    
    if eingabe == "1":
        os.system("cls")
        hallo_sagen("Zahlen addieren Menü")
        zahl_1 = input("Zahl 1: ")
        zahl_2 = input("Zahl 2: ")
        summe = addieren(int(zahl_1), int(zahl_2))
        print("Summe =", summe)
        os.system("pause")
        
    elif eingabe == "2":
        os.system("cls")
        hallo_sagen("Untermenü B")
        os.system("pause")
        
    elif eingabe == "x":
        exit()
        
    else:
        print("Habe ich nicht verstanden!!!")
    