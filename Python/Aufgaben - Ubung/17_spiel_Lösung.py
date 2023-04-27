import random
import os

anzahl = 10
spielfeld_s = [None] * anzahl  # [None, None, None, ....]
spielfeld_c = [None] * anzahl
spielfeld_s[0] = "S"
spielfeld_c[0] = "C"


print("Das sind die Spielfelder:")
print("S =", spielfeld_s)
print("C =", spielfeld_c)
os.system("pause")

while spielfeld_s[-1] != "S" or spielfeld_c[-1] != "C":
    os.system("cls")
    s_pos = spielfeld_s.index("S") # Aktuelle Pos. Spieler
    c_pos = spielfeld_c.index("C") # Aktuelle Pos. Computer
    print("Aktuelle Pos. Spieler =", s_pos)
    print("Aktuelle Pos. Computer =", c_pos)
    
    s_wuerfel = random.randint(1, 6)
    c_wuerfel = random.randint(1, 6)
    print("Würfel Spieler =", s_wuerfel)
    print("Würfel Computer =", c_wuerfel)
    
    spielfeld_s[s_pos] = None
    spielfeld_c[c_pos] = None
    
    if s_pos + s_wuerfel >= len(spielfeld_s):
        spielfeld_s[-1] = "S"
    else:
        spielfeld_s[s_pos + s_wuerfel] = "S"
    
    if c_pos + c_wuerfel >= len(spielfeld_c):
        spielfeld_c[-1] = "C"
    else:
        spielfeld_c[c_pos + c_wuerfel] = "C"
    
    print("S =", spielfeld_s)
    print("C =", spielfeld_c)
    print()
    os.system("pause")

    # sind beide gleichzeitig angekommen?
    if spielfeld_s[-1] == "S" and spielfeld_c[-1] == "C":
        spielfeld_s.extend([None] * 10)
        spielfeld_c.extend([None] * 10)
    elif spielfeld_s[-1] == "S":
        print("Spieler hat gewonnen!")
        break
    elif spielfeld_c[-1] == "C":
        print("Computer hat gewonnen!")
        break
"""
if spielfeld_s[-1] == "S" and spielfeld_c[-1] != "C":
    # Spieler gewinnt!

if spielfeld_s[-1] != "S" and spielfeld_c[-1] == "C":
    # Computer gewinnt!
    
if spielfeld_s[-1] == "S" and spielfeld_c[-1] == "C":
    # Unentschieden!
    # Spiel wird erweitert!
"""