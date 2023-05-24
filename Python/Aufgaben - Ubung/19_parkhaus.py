
# Freier Parkplatz -> None
# Belegter Parkplatz -> str
# - z.b. "VW Golf" oder "Opel Astra" 
import os
# 3 Etagen mit je 4 Plätzen


from colorama import Fore, Back, Style
'''
print(Fore.RED + "Dieser Text ist rot.")
print(Fore.GREEN + "Dieser Text ist grün.")
print(Fore.BLUE + "Dieser Text ist blau.")

print(Back.YELLOW + "Dieser Hintergrund ist gelb.")
print(Back.CYAN + "Dieser Hintergrund ist cyan.")

print(Style.BRIGHT + "Dieser Text ist fett.")

print(Style.RESET_ALL + "Dieser Text ist wieder normal.")
'''


# Funktion aufrufen und das ausgewählte Automodell speichern


parkhaus = [
    ["VW Golf", None, "Opel Astra", None], # 0
    ["Opel Astra", "Opel Astra", "Opel Astra", "VW Golf"], # 1
    [None, None, None, None]               # 2
]


while True:
   
   def auto_model():
    while True:
      os.system("cls")
      print(Fore.GREEN + "PARKPLATZ 1 :", parkhaus [0])
      print("PARKPLATZ 2 :", parkhaus [1])
      print("PARKPLATZ 3 :", parkhaus [2])
      print("------------------------------------------")
      print(Style.RESET_ALL +"Sie haben folgende Optionen:")
      print(Fore.BLUE +"[1] VW Golf")
      print(Fore.BLACK+ "[2] Opel Astra")
      print(Fore.RED + "[3] BMW")
      print(Fore.WHITE + "[4] Nissan")
      print(Fore.LIGHTMAGENTA_EX + "[5] Kia")
      print(Fore.BLUE +"[6] LKW")
      eingabe_auto = input(Style.BRIGHT + "Schreiben Sie bitte, welches Auto-Modell Sie haben >>> ")
      if eingabe_auto == "1":
            return "VW Golf"
      elif eingabe_auto == "2":
         return "Opel Astra"
      elif eingabe_auto == "3":
         return "BMW"
      elif eingabe_auto == "4":
         return "Nissan"
      elif eingabe_auto == "5":
         return "Kia"
      elif eingabe_auto == "6":
         print(" der Parkplatz reicht nicht ")
         input("ENTER")
         (exit)
      else:
         print("Sie haben eine falsche Eingabe gemacht. Bitte wählen Sie entweder 1 oder 2.")
         input("ENTER")

   ausgewaehltes_auto = auto_model()
   print("Sie haben das Automodell", ausgewaehltes_auto, "gewählt.")
   os.system("cls")
   print ( ausgewaehltes_auto)
   print("------------------------------------------")
   
   count = 0

   for etage in parkhaus:
      for parkplatz in etage:
         if parkplatz is None:
               count += 1

   print("Es gibt", count, "leere Parkplätze im Parkhaus.")
   print(Fore.GREEN + "PARKPLATZ 1 :", parkhaus [0])
   print("PARKPLATZ 2 :", parkhaus [1])
   print("PARKPLATZ 3 :", parkhaus [2])
   print("------------------------------------------")
   print(Style.RESET_ALL + "Du hast folgende Optionen ,wo magst parken?")
   print(Fore.BLUE + "[1] ERSE ERAGE")
   print("[2] ZEITE ETAGE")
   print("[3] DRITE ETAGE")
   print("[4] ERSTE FREIE")
   print("[x] Programm beenden" )
   eingabe = input(Style.RESET_ALL +">>> ")
   i = 0

   j = 0         
   if eingabe == "1":
      if None in parkhaus[0]:

         erste_etage = parkhaus[0]
         idx = parkhaus[0].index(None)
         erste_etage = (idx, ausgewaehltes_auto)
         print(erste_etage)
         print( Fore.GREEN + "du parkt in der Erste ertagen auf" , idx + 101 , "Parkpaltznummer")
         input(Style.RESET_ALL +"ENTER")
         
         (exit)

      else:
         input("es ist leider VOLL")
         (exit)
     

   
   elif eingabe == "2":
      if None in parkhaus[1]:
         zweite_etage = parkhaus[1]
         idx = parkhaus[1].index(None)
         
         zweite_etage.remove(None)
         zweite_etage.insert(idx, ausgewaehltes_auto)
         print(zweite_etage)
         print("du parkt in der Zweite ertagen auf" , idx + 101 , "Parkpaltznummer")
         input("ENTER")
         (exit)
      else:
         input("es ist leider VOLL")
         (exit)

   elif eingabe == "3":
      if None in parkhaus[2]:
         drite_etage = parkhaus[2]
         idx = parkhaus[2].index(None)
         
         drite_etage.remove(None)
         drite_etage.insert(idx, ausgewaehltes_auto)
         print(drite_etage)
         print("du parkt in der Drite ertagen auf" , idx + 101 , "Parkpaltznummer")
         input("ENTER")
         (exit)
      else:
         input("es ist leider VOLL")
         (exit)
      
   elif eingabe == "4":
      if None in parkhaus[0]:
         erste_etage = parkhaus[0]
         idx = parkhaus[0].index(None)
         
         erste_etage.remove(None)
         erste_etage.insert(idx, ausgewaehltes_auto)
         print(parkhaus)
         print("du parkt in der Erste ertagen auf" , idx + 101 , "Parkpaltznummer")
         input("ENTER")
         (exit)
      elif None in parkhaus[1]:
         zweite_etage = parkhaus[1]
         idx = parkhaus[1].index(None)
         
         zweite_etage.remove(None)
         zweite_etage.insert(idx, ausgewaehltes_auto)
         print(parkhaus)
         print("du parkt in der Zweite ertagen auf" , idx + 101 , "Parkpaltznummer")
         input("ENTER")
         (exit)
      elif None in parkhaus[2]:
         drite_etage = parkhaus[2]
         idx = parkhaus[2].index(None)
         
         drite_etage.remove(None)
         drite_etage.insert(idx, ausgewaehltes_auto)
         print(parkhaus)
         print("du parkt in der Drite ertagen auf" , idx + 101 , "Parkpaltznummer")
         input("ENTER")
         (exit)

      
      else:
         input("es ist leider VOLL")
         (exit)
   elif eingabe == "x":
        
      print("Auf Wiedersehen!")
      exit()
   
   else:
      print("Das habe ich nicht verstanden!")
      os.system("cls")

      print("exit")
 
      
"""
Entwickle ein Parkhaus-System

In diesem Programm hat der Nutzer folgende Möglichkeiten:
1) Sein Auto in einer bestimmten Etage parken
   - dazu muss der Nutzer eine Etage eingeben
   - anschließend wird ihm der erste freie Platz zugewiesen
   - falls die Etage voll ist, weise den Nutzer darauf hin
2) Sein Auto in dem ersten freien Parkplatz des ganzen(!)
   Parkhauses zu parken
   - ablauf: schleife, welche die etagen durchläuft
             und eine, welche die plätze der aktuellen Etage prüft

Hinweis:
- teste dein Programm mit unterschiedlichen Parkhaus-konfigurationen:
  1) etage 1 voll, nutzer will in etage 1 parken
  2) alle etagen voll, nutzer will in etage 1 parken
  3) alle etagen voll, nutzer wählt menüpunkt 2
  4) alle plätze voll bis auf etage 3 letzter platz, nutzer wählt menüpunkt 2
"""