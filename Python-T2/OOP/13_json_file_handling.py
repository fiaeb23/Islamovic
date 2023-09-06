import json

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ("running", "sky diving", "singing"),
    "age": 35,
    "x": True,
    "y": None,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

# 1) serialization:
# - schreiben in eine json-datei:
#with open(r"Desktop\data.json", "w") as file:
#    json.dump(data, file, indent=4)

# - schreiben in einen json-string:
#print(json.dumps(data))


# 2) deserialization:
# - lesen einer json-datei:
#with open(r"Desktop\data.json") as file:
#    print(type(json.load(file)))
    
# - lesen eines json-strings:
#print(json.loads('{"x": true}'))

""" inhalte einer json-datei lesen:
with open(r"Desktop\orders.json", encoding="utf-8") as file:
    data = json.load(file)
    for order in data:
        print(order["orderDate"])
        print(order["customerNr"])
        print(order["products"])
        print()
"""


""" inhalte einer api lesen:
"""
from urllib import request

url = "https://dummyjson.com/todos"
url = "https://cat-fact.herokuapp.com/facts"
response = request.urlopen(url)
print(response.status)
data = json.load(response)

print(data[0])

#with open(r"Desktop\todo_data.json", "w") as file:
#    json.dump(data, file, indent=4)



""" 
1) Aufgaben mit Lokaler json-Datei:
   A) Finde in der orders.json folgendes heraus:
      - Welcher Kunde (=customerNr) hat die meisten Bestellungen durchgeführt?
      - Wieviele Produkte (=products) haben die Bestellungen im durchschnitt?
        (quantity des jeweiligen products NICHT berücksichtigen sondern einzeln zählen!)
   B) Fasse alle Bestellungen des Kunden mit customerNr 125 in eine json-Datei zusammen        
"""

"""
2) Aufgaben mit API:
   A) Für die API "https://dummyjson.com/todos":
      - Finde heraus, welcher Nutzer (=userId) die meisten todos erledigt hat
   B) Erstelle eine lokale json-Datei mit allen unerledigten todos
"""

"""
BONUS) Suche in der Auflistung der public APIs nach spannenden Daten
       und lies sie ein (evtl. lokal speichern).
"""

#for todo in data['todos']:
#    print(todo["userId"], todo["completed"])
