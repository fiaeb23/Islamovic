""" 
1) Aufgaben mit Lokaler json-Datei:
   A) Finde in der orders.json folgendes heraus:
      - Welcher Kunde (=customerNr) hat die meisten Bestellungen durchgeführt?
      - Wieviele Produkte (=products) haben die Bestellungen im durchschnitt?
        (quantity des jeweiligen products NICHT berücksichtigen sondern einzeln zählen!)
   B) Fasse alle Bestellungen des Kunden mit customerNr 125 in eine json-Datei zusammen        
"""
import json
from urllib import request

"""
with open(r"Desktop\orders.json", encoding="utf-8") as file:
    data = json.load(file)
    
customer_counter = {}
order_sum = 0
orders_customer_125 = []
for elem in data:
    if elem["customerNr"] not in customer_counter:
        customer_counter[elem["customerNr"]] = 0
    customer_counter[elem["customerNr"]] += 1
    
    order_sum += len(elem["products"])
    
    if elem["customerNr"] == 125:
        orders_customer_125.append(elem)
    
max_customer = [None, -1]
for customer_nr, counter in customer_counter.items():
    if counter > max_customer[1]:
        max_customer = [customer_nr, counter]

print("Welcher Kunde (=customerNr) hat die meisten Bestellungen durchgeführt?")
print(f"Kunde {max_customer[0]} mit {max_customer[1]} Bestellungen")
print("Wieviele Produkte (=products) haben die Bestellungen im durchschnitt?")
print(round(order_sum / len(data), 2))


with open(r"Desktop\orders_customer_125.json", "w", encoding="utf-8") as file:
    json.dump(orders_customer_125, file, indent=4)
"""

"""
2) Aufgaben mit API:
   A) Für die API "https://dummyjson.com/todos":
      - Finde heraus, welcher Nutzer (=userId) die meisten todos erledigt hat
   B) Erstelle eine lokale json-Datei mit allen unerledigten todos
"""

url = "https://dummyjson.com/todos"
response = request.urlopen(url)
data = json.load(response) 

user_counter = {}
uncompleted_todos = []
for elem in data["todos"]:
    if elem["userId"] not in user_counter:
        user_counter[elem["userId"]] = 0
    
    if elem["completed"]:
        user_counter[elem["userId"]] += 1
    else:
        uncompleted_todos.append(elem)
   
print(user_counter)
max_user = [None, -1]        
for user, counter in user_counter.items():
    if counter > max_user[1]:
        max_user = [user, counter]
    
print("User mit den meisten erledigten todos:")
print(f"{max_user[0]} hat {max_user[1]} todos erledigt!")    

with open(r"Desktop\uncompleted_todos.json", "w") as file:
    json.dump(uncompleted_todos, file, indent=4)

"""
BONUS) Suche in der Auflistung der public APIs nach spannenden Daten
       und lies sie ein (evtl. lokal speichern).
"""