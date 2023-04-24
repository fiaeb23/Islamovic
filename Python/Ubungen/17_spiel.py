
import random

farben = ["Rot", "Blau"]

spielbrett = list(range(20))

positionen = {
    "Rot": [0],
    "Blau": [10],
}

def zeige_spielbrett():
    for feld in spielbrett:
        if feld in positionen["Rot"]:
            print("R", end=" ")
        elif feld in positionen["Blau"]:
            print("B", end=" ")
        else:
            print(".", end=" ")
        if feld % 10 == 9:
            print()


def wurf():
    return random.randint(1, 6)

def bewege_spieler(spieler):
    print(f"Spieler {spieler} ist am Zug.")
    augenzahl = wurf() + wurf()
    print(f"Du hast {augenzahl} gewürfelt.")
    figuren = positionen[farben[spieler]]
    if all(feld == 19 for feld in figuren):
        print("Du hast bereits alle Figuren im Ziel!")
        return
    auswahl = int(input("Welche Figur möchtest du bewegen? (1-2) ")) - 1
    if auswahl < 0 or auswahl >= len(figuren):
        print("Ungültige Auswahl. Bitte wähle eine Figur zwischen 1 und 2.")
        return
    figur_position = figuren[auswahl]
    neue_position = figur_position + augenzahl
    if neue_position > 19:
        print("Du hast die Ziellinie überschritten.")
        return
    if neue_position in figuren:
        print("Auf diesem Feld steht bereits eine eigene Figur.")
        return
    figuren[auswahl] = neue_position
    zeige_spielbrett()


def mensch_aergere_dich_nicht():
    while True:
        for i in range(2):
            bewege_spieler(i)

mensch_aergere_dich_nicht()













"""""
import random



farben = ["Rot", "Grün", "Blau", "Gelb"]

spielbrett = list(range(40))

positionen = {
    "Rot": [0, 1, 2, 3],
    "Grün": [10, 11, 12, 13],
    "Blau": [20, 21, 22, 23],
    "Gelb": [30, 31, 32, 33]
}

def zeige_spielbrett():
    for feld in spielbrett:
        if feld in positionen["Rot"]:
            print("R", end=" ")
        elif feld in positionen["Grün"]:
            print("G", end=" ")
        elif feld in positionen["Blau"]:
            print("B", end=" ")
        elif feld in positionen["Gelb"]:
            print("Y", end=" ")
        else:
            print(".", end=" ")
        if feld % 10 == 9:
            print()

def wurf():
    return random.randint(1, 6)

def bewege_spieler(spieler):
    print(f"Spieler {farben[spieler]} ist am Zug.")
    augenzahl = wurf() + wurf()
    print(f"Du hast {augenzahl} gewürfelt.")
    figuren = positionen[farben[spieler]]
    if all(feld == 39 for feld in figuren):
        print("Du hast bereits alle Figuren im Ziel!")
        return
    auswahl = int(input("Welche Figur möchtest du bewegen? (1-4) ")) - 1
    figur_position = figuren[auswahl]
    neue_position = figur_position + augenzahl
    if neue_position > 39:
        print("Du hast die Ziellinie überschritten.")
        return
    if neue_position in figuren:
        print("Auf diesem Feld steht bereits eine eigene Figur.")
        return
    figuren[auswahl] = neue_position
    zeige_spielbrett()

def mensch_aergere_dich_nicht():
    while True:
        for i in range(4):
            bewege_spieler(i)

mensch_aergere_dich_nicht()
"""