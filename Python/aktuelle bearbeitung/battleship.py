thisset = {"banana"}

characters_to_remove = ['a', 'e', 'i', 'o', 'u']

for element in thisset:
    for char in characters_to_remove:
        element = element.replace(char, "")

    thisset.remove(element)
    #thisset.add(element)

print(thisset)
