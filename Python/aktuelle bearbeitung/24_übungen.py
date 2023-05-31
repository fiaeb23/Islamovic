"""
Welche Datentypen sollten für die folgenden 
Anforderungen gewählt werden?
"""

"""
a) Es soll eine zentrale Sammlung aller Mitarbeiterdaten existieren. 
   Zu jedem Mitarbeiter stehen folgende Informationen zur Verfügung:
    - Mitarbeiter Id    (Integer)
    - Nachname          (String)
    - Vorname           (String)
    - Geburtsjahr       (Integer)
    - Gehalt            (Float)
"""
# Die Mitarbeiterdaten können beispielsweise in einer Datenbank oder einer anderen geeigneten Datenstruktur gespeichert werden, um eine zentrale Sammlung zu ermöglichen.

"""
b) Es sollen die Ergebnisse einer Abschlussprüfung ohne Personenbezug 
   gespeichert werden. 
   Die Ergebnisse sind Ganzzahlen in 5er Schritten 
   (z.B. 5, 10, 15, 20 etc.) bis maximal 100.
"""
#Ergebnis: Integer / sets

"""
c) Es soll ein Login-Protokoll geführt werden. 
   Dabei gibt es pro Login-Versuch folgende Informationen:
    - E-Mail-Adresse                (String)      
    - War der Login erfolgreich?    (Boolean)
"""

# Das Login-Protokoll kann beispielsweise in einer Datenbank, einer Log-Datei oder einer anderen geeigneten Datenstruktur gespeichert werden.
#tuples 

# EMAIL= "maxmustermann@muster.com"

def login():
    versuche = 0
    while versuche < 3:
        email = input('Geben Sie Ihre E-Mail-Adresse ein: ')
        if email == EMAIL:
            print('Login erfolgreich!')
            log_login(email, True)
            return True
            
        else:
            versuche += 1
            print(f'Falscher PIN! {3 - versuche} Versuch(e) übrig.')
            log_login(email, False)
    
    print('Zu viele falsche Versuche. Das Programm wird beendet.')
    log_login(email, False)
    exit()


def log_login(email, success):
    print(f'Protokoll: E-Mail: {email}, Erfolgreich: {success}')


#login()




"""
d) Definiere eine Funktion, welche überprüft, ob die Datentypen der
Elemente eines Tuples gleich sind

Die Funktion erhält als Parameter eine Variable vom Typ Tupel.

Die Funktion gibt...
-> True zurück, wenn alle Elemente den gleichen Datentypen haben
-> False zurück, wenn nicht
"""
#Parameter ein Tuple und gibt True zurück, wenn alle Elemente den gleichen Datentypen haben, andernfalls gibt sie False zurück.

def check_tuple_data_types(data_tuple):
    return len(set(map(type, data_tuple))) == 1


"""
e) Definiere eine Funktion, welche die einzigartigen Zeichen
eines strings zählt und den Wert als int zurückgibt

Anmerkung: Klein- und Großbuchstaben sind unterschiedliche Zeichen!

"Python"  -> 6
"Pythonn" -> 6
"pPython" -> 7
"""
#Parameter einen String und gibt die Anzahl der einzigartigen Zeichen im String als Integer zurück.

def count_unique_characters(string):
    unique_chars = set(string)
    return len(unique_chars)

print(count_unique_characters("Python"))   # Ausgabe: 6
print(count_unique_characters("Pythonn"))  # Ausgabe: 6
print(count_unique_characters("pPython"))  # Ausgabe: 7
print(count_unique_characters("pPyYthoon")) # Ausgabe: 8


count_unique_characters()

"""
(BONUS)
Definiere eine Funktion, welche die Vokale eines strings entfernt.

Vokale sind die Buchstaben a e i o u bzw. A E I O U

Die Funktion erhält als Parameter einen string

Die Funktion gibt zurück:
- einen string (aber ohne Vokale)

Beispiel:
"abce" -> "bc"
"ae"   -> ""
"xyz"  -> "xyz"
"""
#Parameter einen String und gibt einen String zurück, in dem alle Vokale entfernt wurden.

def remove_vowels(wort):
    vokale = 'aeiouAEIOU'
    result = ''
    for letter in wort:
        if letter not in vokale:
            result += letter
    return result

wort = input("Gebe das Wort ein: ")
result = remove_vowels(wort)
print(result)
