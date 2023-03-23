
# EINGABE
"""
Nutzer gibt ein:
- Siege
- Unentschieden
- Niederlagen
- Tore
- Gegentore
Jede Eingabe sollte in jeweils einer Variable
gespeichert werden!
"""

#s = "siege"
s = int(input ("Gebe Siege ein "))

#u = "Unentschieden "
u = int(input ("Gebe Unentschieden ein "))

#v = "Niederlage"
v = int(input ("Gebe Niederlagen ein "))

#tore = "Tore"
tore = int(input ("Gebe Tore ein "))

#gt = "Gegentore"
gt = int(input ("Gebe Gegentore ein "))

#td = "Tordiverenz"

#p = "Punkte"
p = "Punkte"


# VERARBEITUNG
"""
Ermittlung der verarbeiteten Werte:
- Anzahl Spiele = Siege + Unentschieden + Niederlagen
- Tordifferenz = Tore - Gegentore
- Punkte = Siege*3 + Unentschieden*1 + Niederlagen*0
Achtung:
- Die Eingabe des Nutzers ist IMMER im Textformat (=str)
- Aus einer texteingabe eine Zahl machen -> eingabe = int(eingabe)
"""

spiele = str(s+u+v)
td = str(tore - gt)
p = str(s*3 + u*1 + v*0)


# AUSGABE
"""
Ausgabe der verarbeiteten Werte:
- Wichtig: Beschreibung der Werte
- Notwendig: print()-Funktion
             z.B. print("Anzahl Punkte:", punkte)
"""

print ("Das Team hat " + spiele + " Spiele gespielt" )
print ("Die Tordiverenz liegt bei " + td)
print ("Und hat " + p + " Punkte")
