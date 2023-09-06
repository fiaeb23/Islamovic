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
Aufgabe 2) Welche der folgenden Variablen haben die Eigenschaft `callable`? (5 Punkte)
"""

a = lambda x: x*2
b = "call_me"
c = print(3)
d = max

# Antwort:

a = lambda multiplikation (callable)
b = not callable
c = not callable
d = funktion (callable)




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
sort_1 = ['abc', 'x', 'x', 'xx', 'xxxxxx']
# b)
sort_2 = sorted(unsorted, key=lambda val: val.count("x"))
sort_2 = ['x', 'xx', 'abc', 'x', 'xxxxxx']

# c)
sort_3 = sorted(unsorted, key=lambda val: len(val))
sort_3 = ['x', 'xx',








"""
Aufgabe 4) Definiere eine Lambda-Funktion entsprechend der Anforderungen. (10 Punkte)
"""

""" Anforderungen:
- Die Funktion soll prüfen, ob ein gegebener string `sub_str` in einem set von strings `set_str` vorkommt
- Dabei sollen Teilstrings nicht berücksichtigt werden.
- Sollte ein String gefunden werden, gib True zurück. Ansonsten False.
- siehe Beispielaufrufe
"""

find_str = None

print(find_str({"a", "b", "c"}, "a")) # -> True
print(find_str({"a", "b", "c"}, "d")) # -> False
print(find_str({"aa", "b", "c"}, "a")) # -> False

find_str = lambda set_str, sub_str: any(sub_str.lower() in s.lower() for s in set_str)






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

a = x mit parameter, y ohne parameter, nicht valide
b = valide, x/y parameter, args beliebig viele argumente
c = valide, wie c
d = valide, x/y parameter, z mit standartwert(3), kwargs=dicct  




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

def get_even_nrs() -> list:
    """Return list with all even nrs"""
    pass

#print(get_even_nrs(1, 2, 3))    # -> [2]
#print(get_even_nrs(1, 2, 3, 4)) # -> [2, 4]







"""
Aufgabe 7) Beschreibe folgende Begriffe mit eigenen Worten. (15 Punkte)
"""

# a) Type Hinting
#    - ermöglicht es Entwicklern, den erwarteten Datentyp von Funktionsargumenten und Rückgabewerten anzugeben, 
#       was die Codeverständlichkeit und statische Analyse verbessert, aber keine Auswirkungen auf die tatsächliche Ausführung hat.

# b) Keyword Argument
#    - sind Argumente, die einer Funktion durch explizite Angabe der Parameterbezeichnungen zugewiesen werden, was die Reihenfolge der Argumente unerheblich macht. 

# c) Docstring
#    - eine Zeichenkette (String) in Python, die in Funktionen, Klassen oder Modulen verwendet wird, um eine interne Dokumentation zu erstellen. 
#       Es beschreibt, was die Funktion, Klasse oder das Modul tut, welche Parameter erwartet werden, 
#       welchen Datentyp sie zurückgibt und andere relevante Informationen, um anderen Entwicklern eine klare Verwendung des Codes zu ermöglichen.








"""
Aufgabe 8) Welche Aussagen zu `Lazy Evaluation` sind wahr? Wähle mind. 1 Antwort aus. (10 Punkte)
"""

# a) Ausdrücke werden langsamer ausgewertet, um die CPU zu schonen.
# b) Ausdrücke werden nur dann ausgewertet, wenn sie benötigt werden.
# c) range-Objekte betreiben Lazy Evaluation.
# d) Listen betreiben Lazy Evaluation.

# Antwort:







"""
Aufgabe 9) Welche Aussagen zu `Generators` sind wahr? Wähle mind. 1 Antwort aus. (10 Punkte)
"""

# a) Generator Functions merken sich ihren aktuellen Zustand zur Laufzeit.
# b) Die next()-Funktion kann beliebig oft aufgerufen werden.
# c) (i for i in [1, 2, 3]) erzeugt ein Tupel (1, 2, 3).
# d) Der Befehl yield darf nur ein mal in einer Generator Function vorkommen.

# Antwort:







"""
BONUS) Überführe folgenden Code in List Comprehension. (40 Bonus)
"""

# a)
l = []
for elem in range(10):
    l.append(elem+1)

print(l)
l = None
print(l)


# b)
s = set()
for elem in ["ab", "bb", "ca"]:
    if "a" in elem:
        s.add(elem)

print(s)
s = None
print(s)


# c)
l = []
for nr in range(4):
    for char in ["a", "b"]:
        l.append((nr, char))

print(l)
l = None
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
d = None
print(d)