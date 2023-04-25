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
        if player_positions["A"] == i:
            print("A", end=" ")
        elif player_positions["B"] == i:
            print("B", end=" ")
        else:
            print("_", end=" ")
    print()

    

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
        spielfeld_a[alte_position] = None
        spielfeld_a[neue_position] = player_symbols[player]
    else:
        spielfeld_b[alte_position] = None
        spielfeld_b[neue_position] = player_symbols[player]
    
    zeige_spielfeld()
    os.system("PAUSE")
    return False

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
