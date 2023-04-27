# anzahl = 10
# spielfeld_s = [None] * anzahl  # [None, None, None, ....]
# spielfeld_c = [None] * anzahl
# spielfeld_s[0] = "S"
# spielfeld_c[0] = "C"


# print(spielfeld_s)
# print(spielfeld_c)

import random
import os 

anzahl = 10  # Anzahl der Felder auf dem Spielfeld

player_positions = {"A": 0, "B": 0}
player_symbols = {"A": "A", "B": "B"}

spielfeld = ["_" for _ in range(anzahl)]
spielfeld_a = [None] * anzahl
spielfeld_b = [None] * anzahl


def zeige_spielfeld():
    for i in range(anzahl):
        if spielfeld_a[i]:
            print(spielfeld_a[i], end=" ")
        else:
            print("_", end=" ")
    print()
    for i in range(anzahl):
        if spielfeld_b[i]:
            print(spielfeld_b[i], end=" ")
        else:
            print("_", end=" ")
    print()


    

def bewege_spieler(player):
    print(f"Spieler {player} ist am Zug.")
    würfel = random.randint(1, 6)
    print(f"Du hast {würfel} gewürfelt.")
    alte_position = player_positions[player]                    #posotions rechnung
    player_positions[player] += würfel
    neue_position = player_positions[player]
    print (f"Neue Position: {neue_position}")
    

    if neue_position >= anzahl:
        print(f"Spieler {player} hat gewonnen!")
        return True                                             #schleifen ende 
    
    if player == "A":
        spielfeld_a[alte_position] = None                       # alte position auf None setzen 
        spielfeld_a[neue_position] = player_symbols[player]     # neue Position mit Spieler Symbol füllen
    else:
        spielfeld_b[alte_position] = None
        spielfeld_b[neue_position] = player_symbols[player]
    
    zeige_spielfeld()
    os.system("PAUSE")
    return False                                                #schleife weitetr laufen lassen

def neues_spiel():
    global spielfeld, spielfeld_a, spielfeld_b, player_positions, anzahl
    while True:
        for player in player_positions:
            if bewege_spieler(player):
                if all([player_positions[player] >= anzahl for player in player_positions]):
                    print("Beide Spieler haben gleichzeitig das Ziel erreicht!")
                    print("Das Spielfeld wird um 10 Felder erweitert.")
                    anzahl += 10
                    spielfeld = ["_" for _ in range(anzahl)]
                    spielfeld_a = [None] * anzahl
                    spielfeld_b = [None] * anzahl
                    player_positions = {player: 0 for player in player_positions}
                    zeige_spielfeld()
                else:
                    return


zeige_spielfeld()
neues_spiel()





'''
# VARIATION ZWEI 

import random
import os 

anzahl = 10  # Anzahl der Felder auf dem Spielfeld

player_positions = {"A": 0, "B": 0}
player_symbols = {"A": "A", "B": "B"}

spielfeld_a = ["_" for _ in range(anzahl)]
spielfeld_b = ["_" for _ in range(anzahl)]


def zeige_spielfeld():
    print("Spielfeld A:", spielfeld_a)
    print("Spielfeld B:", spielfeld_b)

def bewege_spieler(player):
    print(f"Spieler {player} ist am Zug.")
    würfel = random.randint(1, 6)
    print(f"Du hast {würfel} gewürfelt.")
    alte_position = player_positions[player]
    player_positions[player] += würfel
    neue_position = player_positions[player]
    print (f"Neue Position: {neue_position}")
    

    if neue_position >= anzahl:
        print(f"Spieler {player} hat gewonnen!")
        return True
    
    if player == "A":
        spielfeld_a[alte_position] = "_"                       # alte position auf None setzen 
        spielfeld_a[neue_position] = player_symbols[player]     # neue Position mit Spieler Symbol füllen
    else:
        spielfeld_b[alte_position] = "_"
        spielfeld_b[neue_position] = player_symbols[player]
    
    zeige_spielfeld()
    os.system("PAUSE")
    return False

def neues_spiel():
    global spielfeld_a, spielfeld_b, player_positions, anzahl
    while True:
        alte_positionen = list(player_positions.values())
        for player in player_positions:
            if bewege_spieler(player):
                if all([player_positions[player] >= anzahl for player in player_positions]):
                    print("Beide Spieler haben gleichzeitig das Ziel erreicht!")
                    print("Das Spielfeld wird um 10 Felder erweitert.")
                    anzahl += 10
                    spielfeld_a = ["_" for _ in range(anzahl)]
                    spielfeld_b = ["_" for _ in range(anzahl)]
                    player_positions = {player: 0 for player in player_positions}
                    zeige_spielfeld()
                else:
                    continue
        # beide Spieler müssen gewürfelt haben, um das Spiel fortzusetzen
        if all([player_positions[player] >= alte_position for player, alte_position in zip(player_positions.keys(), alte_positionen)]):
            alte_positionen = list(player_positions.values())
            continue
        else:
            print("Beide Spieler müssen gewürfelt haben! Das Spiel wird beendet.")
            return

def spiel_menu():
    while True:
        print("\n--- Spielmenü ---")
        print("1. Neues Spiel starten")
        print("2. Programm beenden")
        auswahl = input("Bitte wählen Sie eine Option: ")
        if auswahl == "1":
            neues_spiel()
        elif auswahl == "2":
            print("Programm wird beendet.")
            return
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine der verfügbaren Optionen.")

spiel_menu()
'''