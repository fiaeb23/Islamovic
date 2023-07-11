"""
Aufgabe 1:
Wandle die folgenden Zeilen in LC um.
"""

listy = []
for i in range(1000):
    listy.append(i)

print(listy)

"""
Aufgabe 2:
Wandle die folgenden Zeilen in LC um.
"""

fruits = {"apple", "banana", "cherry", "kiwi", "mango"}

fav_fruits = set()
for elem in fruits:
    if "e" in elem:
        fav_fruits.add(elem)

print(fav_fruits)

"""
Aufgabe 3:
Wandle die folgenden Zeilen in LC um.
"""

grades = [("Albert", 2), ("Bruno", 4), ("Carla", 1)]

_grades = {}
for name, grade in grades:
    _grades[name] = grade

print(_grades)


"""
Bonus:
Implementiere die folgenden Funktionen für den Datensatz articles.
Orientiere dich an den Kommentaren innerhalb der Funktion.
Hinweis: Versuche es mit LC zu lösen. Falls nicht möglich, dann
versuche es zunächst konventionell und anschließend mit LC.

Beispielaufrufe findest du unten.
"""

def filter_by_max_price(seq:list[dict], max_price:float) -> list[dict]:
    """Returns a list with all articles that cost less than (or are equal to) max_price."""
    pass


def get_sublists_by_key(seq:list[dict], key:str) -> dict[str, list]:
    """Groups all elements of seq by key into a dict."""
    """example:
    {
        "black": [...],
        "white": [...],
        "beige": [...]
    }
    """
    pass

articles = [
    {"name": "JABRA ELITE 7 ACTIVE", "color": "black", "category": "headphones", "price": 234.23},
    {"name": "SONY WF-C500", "color": "white", "category": "headphones", "price": 139.44},
    {"name": "JBL Tune 230NC", "color": "black", "category": "headphones", "price": 3252.21},
    {"name": "SENNHEISER SPORT", "color": "beige", "category": "headphones", "price": 954.25},
    {"name": "XIAOMI Redmi Buds 3 Lite", "color": "black", "category": "headphones", "price": 21.1},
    {"name": "APPLE AirPods Pro ", "color": "white", "category": "headphones", "price": 323.49},
    {"name": "Sonnenblumenöl", "color": "gold", "category": "other", "price": float("inf")}
]

print(filter_by_max_price(articles, 100.0))
# Erwartete Ausgabe: [{'name': 'XIAOMI Redmi Buds 3 Lite', 'color': 'black', 'category': 'headphones', 'price': 21.1}]
print()

print(get_sublists_by_key(articles, "color"))
"""Erwartete Ausgabe: 
{
'black': [  {'name': 'JABRA ELITE 7 ACTIVE', 'color': 'black', 'category': 'headphones', 'price': 234.23}, 
            {'name': 'JBL Tune 230NC', 'color': 'black', 'category': 'headphones', 'price': 3252.21}, 
            {'name': 'XIAOMI Redmi Buds 3 Lite', 'color': 'black', 'category': 'headphones', 'price': 21.1}], 
'white': [  {'name': 'SONY WF-C500', 'color': 'white', 'category': 'headphones', 'price': 139.44}, 
            {'name': 'APPLE AirPods Pro ', 'color': 'white', 'category': 'headphones', 'price': 323.49}], 
'beige': [  {'name': 'SENNHEISER SPORT', 'color': 'beige', 'category': 'headphones', 'price': 954.25}], 
'gold': [   {'name': 'Sonnenblumenöl', 'color': 'gold', 'category': 'other', 'price': inf}]
}
"""
print()

print(get_sublists_by_key(articles, "category"))
"""Erwartete Ausgabe:
{
'headphones': [{'name': 'JABRA ELITE 7 ACTIVE', 'color': 'black', 'category': 'headphones', 'price': 234.23}, {'name': 'SONY WF-C500', 'color': 'white', 'category': 'headphones', 'price': 139.44}, {'name': 'JBL Tune 230NC', 'color': 'black', 'category': 'headphones', 'price': 3252.21}, {'name': 'SENNHEISER SPORT', 'color': 'beige', 'category': 'headphones', 'price': 954.25}, {'name': 'XIAOMI Redmi Buds 3 Lite', 'color': 'black', 'category': 'headphones', 'price': 21.1}, {'name': 'APPLE AirPods Pro ', 'color': 'white', 'category': 'headphones', 'price': 323.49}], 
'other': [{'name': 'Sonnenblumenöl', 'color': 'gold', 'category': 'other', 'price': inf}]
}
"""

