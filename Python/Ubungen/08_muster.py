# """
# Erzeuge folgendes Muster mithilfe einer while-Schleife:

# *
# **
# ***
# ****

# Die Anzahl der "*" in der letzten Reihe hängt von der 
# Variable `anzahl` ab.
# """

# anzahl = 4

# while ???:
#     ...
    

# """
# Erzeuge folgendes Muster mithilfe einer while-Schleife:

# 1
# 12
# 123
# 1234

# Die letzte Zahl in der letzten Zeile hängt von der Variable
# `anzahl` ab.
# """

# anzahl = 4

anzahl = 15

a = 1                           # i = beginn der anzahl der schleife 
while a <= anzahl:              # abfrage 
    b = 1                       # festlegung von x
    while b <= a:               # abfrage x soll gelich i sein (8)
        print(b, end='')        # ausgabe jede zahl in der gleichen zeile
        b += 1                  # größe der Schritte
    print()
    a += 1                     # anzahl der beigefügten Zahlen
