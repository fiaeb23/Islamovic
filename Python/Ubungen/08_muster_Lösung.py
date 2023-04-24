"""
Erzeuge folgendes Muster mithilfe einer while-Schleife:

*
**
***
****

Die Anzahl der "*" in der letzten Reihe hängt von der 
Variable `anzahl` ab.
"""

anzahl = 4
counter = 1


while counter <= anzahl:
    print("*" * counter)
    counter = counter + 1
    

"""
Erzeuge folgendes Muster mithilfe einer while-Schleife:

1
12
123
1234

Die letzte Zahl in der letzten Zeile hängt von der Variable
`anzahl` ab.
"""

anzahl = 4
counter = 1
text = ""

while counter <= anzahl:
    text = text + str(counter)
    print(text)
    counter = counter + 1