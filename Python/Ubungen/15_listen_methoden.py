
l = ["a", "b", "c", "d"]

print(l[1])   # "b"
print(l[3])   # "d"
print(l[-2])  # "c"
print(l[-4])  # "a"
print(l[1:3]) # ["b", "c"]
print(l[:-1]) # ["a", "b", "c"]
print(l[:])   # ["a", "b", "c", "d"] -> Kopie (d.h. neue Adresse)
print(l)      # ["a", "b", "c", "d"] -> Original (d.h. gleiche Adresse)

l2 = l    # l2 & l haben die gleiche Adresse
l3 = l[:] # l3 & l haben nicht die gleiche Adresse

l[2] = "x"
print(l) # ["a", "b", "x", "d"]
l[0:2] = ["A", "B"]
print(l) # ["A", "B", "x", "d"]
l.append(10)  # füge 10 ans Ende hinzu
print(l) # ["A", "B", "x", "d", 10]
l.extend([True, False]) # füge True und False ans Ende hinzu
print(l) # ["A", "B", "x", "d", 10, True, False]
l.insert(4/2+1, "abc")  # füge "abc" in Position 3 hinzu
print(l) # ["A", "B", "x", "abc", "d", 10, True, False]

# entferne das erste Element:
l.remove("A") # entferne genau 1 "A" (egal wo es ist)
del l[0]      # entferne das erste Element der Liste
l.pop(0)      # entferne das erste Element der Liste & gebe es zurück

l = ["C", "C", "A", "C"]
while "C" in l:   # solange mind. 1 "C" in l drin ist...
    l.remove("C") # ...entferne das erste "C"
print(l) # ["A"]

l.clear() # entferne alle Elemente einer Liste
l = ["A", "B", "C", "A"]
l.index("A") # 0 (.index gibt den Index zurück, indem das Element
#                 zum ersten mal gefunden wurde)
l.count("A") # 2
l.sort() # liste sortieren (alphabetisch bzw. aufsteigend)
l = [1, 2, 3]
l.reverse() # liste umdrehen
print(l) # [3, 2, 1]
l.copy()
l2 = l[:]

#      0,   1,   2,   3
l = ["A", "B", "C", "A"]
len(l) # 4

i = 0
while i < len(l): # i < 4
    print(l[i])
    i = i + 1




