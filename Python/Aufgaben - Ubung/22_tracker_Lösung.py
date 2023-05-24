tracker_db = [
#   [<datum>,    <gelaufene_meter>]
    ["14.03.23", 3000], # Lauf 1
    ["21.03.23", 3400], # Lauf 2
    ["01.04.23", 2200], # Lauf 3
    ["06.04.23", 3800], # Lauf 4
    ["13.04.23", 4000]  # Lauf 5
]

# beachte:
# - tracker_db kann leere Liste sein!
# - tracker_db kann aus beliebig vielen Elementen bestehen!

"""
Finde folgendes für die tracker_db heraus:
1) Wie oft ist der Nutzer gelaufen?
2) Wieviel km ist der Nutzer in summe gelaufen?
3) Wieviel km läuft der Nutzer im Durchschnitt?

BONUS)
B1) Wie oft hat der Nutzer sich verbessert?
    - Verbesserung = aktueller Lauf ist besser als der vorherige
    - erw. Wert = 3
B2) Wieviel ist der Nutzer pro Monat gelaufen?
    - Bilde anzahl, summe (km) & durchschnitt (km) pro Monat
"""

# 1) Wie oft ist der Nutzer gelaufen?
print("Der Nutzer ist", len(tracker_db), "mal gelaufen!")

# 2) Wieviel km ist der Nutzer in summe gelaufen?
summe_meter = 0
anzahl_verbesserungen = 0
letzter_lauf = float("inf")
for datum, meter in tracker_db:
    summe_meter = summe_meter + meter
    
    if meter > letzter_lauf:
        anzahl_verbesserungen += 1
    
    letzter_lauf = meter

    
print("Der Nutzer ist in Summe", summe_meter/1000, "km gelaufen!")

# 3) Wieviel km läuft der Nutzer im Durchschnitt?
if len(tracker_db) > 0:
    print("Im Durchschnitt ist der Nutzer", summe_meter/len(tracker_db)/1000, "km gelaufen!")

"""
anzahl_verbesserungen = 0
for i in range(len(tracker_db)-1): # [0, 1, 2, 3]

    if tracker_db[i][1] < tracker_db[i+1][1]:
        anzahl_verbesserungen += 1
"""

# B1) Wie oft hat der Nutzer sich verbessert?
print("Der Nutzer hat sich", anzahl_verbesserungen, "mal verbessert!")

# B2) Wieviel ist der Nutzer pro Monat gelaufen?
monate_anzahl = [0] * 12  # [0, 0, ...., 0, 0]
monate_summe = [0] * 12  # [0, 0, ...., 0, 0]

for datum, meter in tracker_db:

    # 1. Möglichkeit: direkt adressieren
    # "14.03.23" -> "03"
    tag = datum[:2]
    monat = datum[3:5]
    jahr = datum[6:]
    
    # 2. Möglichkeit: string teilen
    # "14.03.23" -> ["14", "03", "23"] -> "03"
    tag = datum.split(".")[0]
    monat = datum.split(".")[1]
    jahr = datum.split(".")[2]
    
    monat = int(monat) # "03" -> 3
    
    monate_anzahl[monat-1] += 1
    monate_summe[monat-1] += meter
    
for i in range(12): # [0, 1, 2, 3, ..., 10, 11]
    
    if monate_anzahl[i] == 0:
        continue
        
    print("Im Monat", i+1, "ist der Nutzer:")
    print(monate_anzahl[i], "mal gelaufen!")
    print("In Summe waren das", monate_summe[i]/1000, "km!")
    print("Im Schnitt waren das", round(monate_summe[i]/monate_anzahl[i]/1000, 2), "km!")
    print()
    
    
    
