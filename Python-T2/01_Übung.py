"""
Beispiel 1: List Comprehension
"""
random_nrs = [54, 95, 86, 24, 85, 27, 40, 73, 58, 28]

out_list_0 = []
for elem in random_nrs:
    if elem % 2 == 0:
        out_list_0.append(elem)

out_list_1 = [elem for elem in random_nrs if elem % 2 == 0]

print(out_list_0 == out_list_1) # -> True
print(out_list_0) # -> [54, 86, 24, 40, 58, 28]
print(out_list_1) # -> [54, 86, 24, 40, 58, 28]



"""
Übung 1: Online Shop
"""

articles = [
    {"name": "JABRA ELITE 7 ACTIVE", "color": "black"},
    {"name": "SONY WF-C500", "color": "white"},
    {"name": "JBL Tune 230NC", "color": "black"},
    {"name": "SENNHEISER SPORT", "color": "beige"},
    {"name": "XIAOMI Redmi Buds 3 Lite", "color": "black"},
    {"name": "APPLE AirPods Pro ", "color": "white"}
]

user_color = []

filtered_articles = []

if len(user_color) == 0:
    filtered_articles = articles.copy()
else:
    for elem in articles:
        # elem = {"name": "JABRA ELITE 7 ACTIVE", "color": "black"}
        # elem["color"] = "black"
        if elem["color"] in user_color:
            filtered_articles.append(elem)

print(filtered_articles)

if len(user_color) == 0:
    filtered_articles = articles.copy()
else:
    filtered_articles = [elem for elem in articles if elem["color"] in user_color]

print(filtered_articles)

# 1. Schleifendurchlauf:
elem = {"name": "JABRA ELITE 7 ACTIVE", "color": "black"}
elem["color"] = "black"
user_color = "black"
elem["color"] == user_color # True
# "füge elem der liste 'filtered_articles' hinzu

# 2. Schleifendurchlauf:
elem = {"name": "SONY WF-C500", "color": "white"}
elem["color"] = "white"
user_color = "black"
elem["color"] == user_color # False
# "füge elem der liste 'filtered_articles' NICHT hinzu




"""
Beispiel 2: LC mit nested loops
"""

chars = ["a", "b", "c"]
nrs = [10, 20, 30, 40, 50]

chars_nrs = []
for c in chars:
    for i in nrs:
        chars_nrs.append((c, i))

print(chars_nrs)
# [('a', 10), ('a', 20), ('a', 30), ('a', 40), ('a', 50), 
#  ('b', 10), ('b', 20), ('b', 30), ('b', 40), ('b', 50), 
#  ('c', 10), ('c', 20), ('c', 30), ('c', 40), ('c', 50)]

chars_nrs = [(c, i) for c in chars for i in nrs]

print(chars_nrs)
# [('a', 10), ('a', 20), ('a', 30), ('a', 40), ('a', 50), 
#  ('b', 10), ('b', 20), ('b', 30), ('b', 40), ('b', 50), 
#  ('c', 10), ('c', 20), ('c', 30), ('c', 40), ('c', 50)]


"""
Beispiel 3: Comprehension mit anderen Datentypen
"""
# tuple
print((i for i in range(10)))
print(tuple(i for i in range(10)))

# set
print({i for i in [1, 2, 1, 1, 2]})

# dict
print({f"{i}²": i**2 for i in range(10)})


