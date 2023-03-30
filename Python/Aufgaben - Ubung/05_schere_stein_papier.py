"""
Übung 2:
Implementiere ein Schere-Stein-Papier Spiel in Python.
"""
import random

bot_hand = random.choice(["Schere", "Stein", "Papier"])
usr_hand = input("Wähle aus Schere, Stein, Papier: ")

print("Computer wählt:", bot_hand)

if usr_hand == bot_hand:
    print("Unentschieden!")
    
elif usr_hand == "Schere" and bot_hand == "Papier":
    print("Gewonnen!")
elif usr_hand == "Stein" and bot_hand == "Schere":
    print("Gewonnen!")
elif usr_hand == "Papier" and bot_hand == "Stein":
    print("Gewonnen!")

elif usr_hand == "Schere" and bot_hand == "Stein":
    print("Verloren!")
elif usr_hand == "Stein" and bot_hand == "Papier":
    print("Verloren!")
elif usr_hand == "Papier" and bot_hand == "Schere":
    print("Verloren!")
    
else:
    print("Fehlerhafte Eingabe!")