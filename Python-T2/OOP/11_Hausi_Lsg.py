"""
Erstelle eine Uhr in Python mithilfe von OOP.

Dazu soll eine Klasse mit folgenden Attributen definiert werden:
- Stunden (int)
- Minuten (int)
- Sekunden (int)
"""
class Clock:
    
    
    def __init__(self, hours: int, minutes: int, seconds: int):
        """
        1. Aufgabe:
        Definiere einen Konstruktor für deine Klasse:
        - Dieser erhält 3 Parameter:
          Stunden, Minuten, Sekunden
        - Überlege dir, welche Maximalwerte pro Attribut erlaubt sein sollten
        - Sollte einer der 3 Werte fehlerhaft sein (z.b. negativ), soll eine Exception erscheinen
          BONUS) Überlege dir, welche spezielle Fehlermeldung sich anbietet.
        """
        if 0 <= hours <= 23:
            self.__hours = hours
        else:
            raise ValueError("Stunden nur zwischen 00 und 23")
            
        if 0 <= minutes <= 59:
            self.__minutes = minutes
        else:
            raise ValueError("Minuten nur zwischen 00 und 59")
            
        if 0 <= seconds <= 59:
            self.__seconds = seconds
        else:
            raise ValueError("Sekunden nur zwischen 00 und 59")

    def __repr__(self) -> str:
        """
        2. Aufgabe:
        Definiere eine sinnvolle Repräsentation für deine Klasse:
        - Objekte deiner Klasse sollen mit der print() Funktion aufgerufen werden können
        - Die Uhrzeit soll in folgendem Format ausgegeben werden können:
          HH:MM:SS # z.b. 20:08:41
        - Tipp: Nutze formatted strings
        - Tipp2: Schau dir die str.zfill() Methode an
        """
        h, m, s = str(self.__hours), str(self.__minutes), str(self.__seconds)
        return f"{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}"

    def __add__(self, other: int):
        """
        3. Aufgabe:
        Definiere eine Methode, um die Anzahl der Sekunden zu erweitern:
        - Objekte deiner Klasse sollen mit dem Plus Operator (+) zurecht kommen
        - Beim Addieren mit int-Werten sollen Sekunden hinzugefügt werden können
        - Beispiel: print(Clock(20, 8, 41) + 3) -> "20:08:44"
        """
        return Clock.from_seconds(len(self) + other)

    def __len__(self) -> int:
        """
        4. Aufgabe:
        Definiere eine Methode, um schnell an die Gesamtanzahl der Sekunden zu kommen:
        - Objekte deiner Klasse sollen als Parameter von len() genutzt werden können
        - Der Rückgabewert soll dabei die Gesamtanzahl der Sekunden sein
        - Beispiel: len(Clock(1, 1, 1)) -> 3600 + 60 + 1 -> 3661
        """
        return self.__hours*3600 + self.__minutes*60 + self.__seconds
        
    def __bool__(self) -> bool:
        """
        5. Aufgabe:
        Definiere eine Methode, um schnell zu prüfen, ob es vor- oder nachmittags ist:
        - Objekte deiner Klasse sollen als Parameter von bool() genutzt werden können
        - Der Rückgabewert soll True sein, wenn es nachmittags (ab 12:00:01 bis 00:00:00) ist
        -                       False              vormittags  (ab 00:00:01 bis 12:00:00)
        - Beispiel: bool(Clock(2, 4, 3)) -> False
                    bool(Clock(21, 4, 3)) -> True
        """
        return self.__hours > 12 or (self.__hours == 12 and (self.__seconds >= 1 or self.__minutes >= 1))
       
    @classmethod
    def from_seconds(cls, seconds: int):
        """
        BONUS 2) Erweitere deine Klasse um eine classmethod:
        - Dadurch soll ein Objekt der Klasse nur mit der Angabe von Sekunden erstellt werden können
        """
        hours = seconds // 3600
        rest = seconds % 3600
        minutes = rest // 60
        seconds = rest % 60
        return cls(hours, minutes, seconds)
        

x = Clock(20, 8, 59)
x = x + 1
print(x)
x = x + 1
print(x)

print(
    bool(Clock(12,0,1)),
    bool(Clock(12,0,0)),
    bool(Clock(14,0,0))
)

print(
    Clock.from_seconds(3600),
    Clock.from_seconds(3661)
)








