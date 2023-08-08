"""
Aufgabe 1) Durch welche Funktionsweise des Decorators wird die Funktion `divide` hier erweitert? (15 Punkte)
"""

def deco(func):

    def wrapper(a, b):
        if b == 0:
            return None
        else:
            return func(a, b)

    return wrapper

@deco
def divide(a, b):
    return a / b

# Antwort:
"""
- division durch 0 wird verhindert
  (ZeroDivisionError wird verhindert)
"""






"""
Aufgabe 2) Welche der folgenden Variablen haben die Eigenschaft `callable`? (5 Punkte)
"""

a = lambda x: x*2
b = "call_me"
c = print(3)
d = max

# Antwort:
"""
a ist callable -> a ist eine lambda-definition
d ist callable -> d ist (quasi) die max-funktion
"""






"""
Aufgabe 3) Welcher dieser Aufrufe sortiert die Liste entsprechend der Anforderung? (10 Punkte)
"""

unsorted = ["abc", "x"*6, "x", "axx", "xx"]

""" Anforderungen:
- Die Liste soll so sortiert werden, dass das Element mit den wenigsten "x" am Anfang steht
- Sollten 2 Elemente die gleiche Anzahl "x" haben, so spielt die Reihenfolge dieser keine Rolle
- Es soll absteigend sortiert werden (vom Element mit keinem "x" zum Element mit den meisten "x")
- korrekt sortiert sieht die Liste so aus: ['abc', 'x', 'axx', 'xx', 'xxxxxx']
                                           # 'axx' und 'xx' können auch vertauscht sein!
"""

# a)
sort_1 = sorted(unsorted, key=lambda val: val[0])

# b)
sort_2 = sorted(unsorted, key=lambda val: val.count("x"))

# c)
sort_3 = sorted(unsorted, key=lambda val: len(val))

# Antwort: 
"""
b)
val.count("x") zählt wieviele "x" im string vorkommen
und nutzt das ergebnis als sortierwert
"""






"""
Aufgabe 4) Definiere eine Lambda-Funktion entsprechend der Anforderungen. (10 Punkte)
"""

""" Anforderungen:
- Die Funktion soll prüfen, ob ein gegebener string `sub_str` in einem set von strings `set_str` vorkommt
- Dabei sollen Teilstrings nicht berücksichtigt werden.
- Sollte ein String gefunden werden, gib True zurück. Ansonsten False.
- siehe Beispielaufrufe
"""

find_str = lambda set_str, sub_str: sub_str in set_str

print(find_str({"a", "b", "c"}, "a")) # -> True
print(find_str({"a", "b", "c"}, "d")) # -> False
print(find_str({"aa", "b", "c"}, "a")) # -> False







"""
Aufgabe 5) Welche dieser Funktionsdefinitionen sind valide? (10 Punkte)
"""

# a)
"""
def f(x=3, y):
    pass
"""

# b)
"""
def f(x, y, *args):
    pass
"""

# c)
"""
def f(x, y, *z):
    pass
"""

# d)
"""
def f(x, y, z=3, **kwargs):
    pass
"""

# Antwort:
"""
b, c, d
"""






"""
Aufgabe 6) Definiere folgende Funktion um, sodass sie mit einer beliebigen Anzahl Parameter zurechtkommt. (15 Punkte)
"""

def get_even_nrs(nr_0, nr_1, nr_2) -> list:
    """Return list with all even nrs"""
    even_nrs = []
    if nr_0 % 2 == 0:
        even_nrs.append(nr_0)
    if nr_1 % 2 == 0:
        even_nrs.append(nr_1)
    if nr_2 % 2 == 0:
        even_nrs.append(nr_2)

    return even_nrs

#print(get_even_nrs(1, 2, 3))    # -> [2]
#print(get_even_nrs(1, 2, 3, 4)) # -> TypeError

def get_even_nrs(*args) -> list:
    """Return list with all even nrs"""
    even_nrs = []
    for nr in args:
        if nr % 2 == 0:
            even_nrs.append(nr)
    
    return even_nrs

#print(get_even_nrs(1, 2, 3))    # -> [2]
#print(get_even_nrs(1, 2, 3, 4)) # -> [2, 4]







"""
Aufgabe 7) Beschreibe folgende Begriffe mit eigenen Worten. (15 Punkte)
"""

# a) Type Hinting
#    - Beschreibung von Parameter- und Rückgabetypen
#    - Keine Pflicht sondern Hinweis!

# b) Keyword Argument
#    - Parameter mit Default-Wert (z.B. def f(x=10): ...)
#    - Bei Aufruf: Default-Wert kann überschrieben werden: (z.B. f(x=3))

# c) Docstring
#    - Standardisierte Beschreibung einer Funktion:
#      - Eingabe
#      - Funktionsweise
#      - Rückgabewert







"""
Aufgabe 8) Welche Aussagen zu `Lazy Evaluation` sind wahr? Wähle mind. 1 Antwort aus. (10 Punkte)
"""

# a) Ausdrücke werden langsamer ausgewertet, um die CPU zu schonen.
# b) Ausdrücke werden nur dann ausgewertet, wenn sie benötigt werden.
# c) range-Objekte betreiben Lazy Evaluation.
# d) Listen betreiben Lazy Evaluation.

# Antwort:
# b, c






"""
Aufgabe 9) Welche Aussagen zu `Generators` sind wahr? Wähle mind. 1 Antwort aus. (10 Punkte)
"""

# a) Generator Functions merken sich ihren aktuellen Zustand zur Laufzeit.
# b) Die next()-Funktion kann beliebig oft aufgerufen werden.
# c) (i for i in [1, 2, 3]) erzeugt ein Tupel (1, 2, 3).
# d) Der Befehl yield darf nur ein mal in einer Generator Function vorkommen.

# Antwort:
# a






"""
BONUS) Überführe folgenden Code in List Comprehension. (40 Bonus)
"""

# a)
l = []
for elem in range(10):
    l.append(elem+1)

print(l)
l = [elem+1 for elem in range(10)]
print(l)


# b)
s = set()
for elem in ["ab", "bb", "ca"]:
    if "a" in elem:
        s.add(elem)

print(s)
s = {elem for elem in ["ab", "bb", "ca"] if "a" in elem}
print(s)


# c)
l = []
for nr in range(4):
    for char in ["a", "b"]:
        l.append((nr, char))

print(l)
l = [(nr, char) for nr in range(4) for char in ["a", "b"]]
print(l)


# d)
name_list = ["Anna", "Bob", "Ali"]
char_tup = ("a", "b", "c")

d = {}
for name in name_list:
    for char in char_tup:
        if char not in d:
            d[char] = []
        if name[0].lower() == char:
            d[char].append(name)

print(d)
d = {char: [name for name in name_list if name[0].lower() == char] for char in char_tup}
print(d)


