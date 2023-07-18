"""
1) Definiere eine Funktion, welche zählt wie oft bestimmte Zeichen in
   einem string vorkommen. Dabei sollen die Zeichen, die gezählt werden
   beim Funktionsaufruf angegeben werden (=flexibel sein).
   
   z.B. f("Python", "y") -> {"y": 1}
        f("Banane", "a", "n", "e") -> {"a": 2, "n": 2, "e": 1}
        f("Tisch", "x", "y") -> {"x": 0, y: 0}
        
2) Dokumentiere die Funktionen mit einem Docstring.
"""

def get_chars(word: str, *chars: tuple[str]) -> dict[str, int]:
    """
    count all occurences of chars in word
    
    Arguments:
        word: a str which is checked for chars
        chars: chars that are searched for in word
        
    Returns:
        dict with all occurences of all chars in word
    """
    
    out_dict = {}
    for elem in set(chars):
        # out_dict["y"] = 1
        out_dict[elem] = word.count(elem)
        
    return out_dict
    
    
print(
    get_chars("Python", "y"),
    get_chars("Banane", "a", "n", "e"),
    get_chars("Tisch", "x", "y", "y"),
    get_chars("Handy"),
    sep = "\n"
)