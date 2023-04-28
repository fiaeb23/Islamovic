"""
Entwickle ein Programm, um für ein gegebenes TicTacToe-Spielfeld
einen Sieger bzw. ein Unentschieden zu ermitteln.
"""

ttt = [
#     0    1    2
    ["O", "X", "O"],     # 0
    [None, "O", None],     # 1
    ["O", None, "X"]   # 2
]

anzahl_gewinne = 0

# horizontale Überprüfung
i = 0
while i < len(ttt):
    if ttt[i][0] == ttt[i][1] == ttt[i][2] and ttt[i][0] != None:
        print("Sieger horizontal in Reihe", i+1)
        print("Gewonnen hat:", ttt[i][0])
        anzahl_gewinne = anzahl_gewinne + 1
        break
    i = i + 1
    
# vertikale Überprüfung
i = 0
while i < len(ttt):
    if ttt[0][i] == ttt[1][i] == ttt[2][i] and ttt[0][i] != None:
        print("Sieger vertikal in Spalte", i+1)
        print("Gewonnen hat:", ttt[0][i])
        anzahl_gewinne = anzahl_gewinne + 1
        break
    i = i + 1

# diagonale Überprüfung
if ttt[0][0] == ttt[1][1] == ttt[2][2] and ttt[1][1] != None:
    print("Sieger diagonal von oben-links nach unten-rechts")
    print("Gewonnen hat:", ttt[1][1])
    anzahl_gewinne = anzahl_gewinne + 1
    
elif ttt[2][0] == ttt[1][1] == ttt[0][2] and ttt[1][1] != None:
    print("Sieger diagonal von unten-links nach oben-rechts")
    print("Gewonnen hat:", ttt[1][1])
    anzahl_gewinne = anzahl_gewinne + 1
    
if anzahl_gewinne > 1:
    print("Evtl. Fehler im Spiel!")

"""
i = 0
if ttt[i][0] == ttt[i][1] == ttt[i][2]:

i = 1
if ttt[i][0] == ttt[i][1] == ttt[i][2]:

i = 2
if ttt[i][0] == ttt[i][1] == ttt[i][2]:
"""
