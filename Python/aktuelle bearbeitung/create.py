# Password Generator
"""
import random

chars = 'abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZ!$@%&*().,-€?0123456789'

number = input('Anzahl der erstellten Passwörter: ')
number = int(number)

length = input('Länge des Passworts: ')
length = int(length)

passwords = []

for _ in range(number):
    password = ''
    for i in range(length):
        password += random.choice(chars)
        if (i + 1) % 3 == 0 and i + 1 != length:
            password += '-'
    passwords.append(password)

formatted_passwords = '\n'.join(passwords)
print("Generiertes Passwort:\n" + formatted_passwords)
"""

"""""
#countdown
import time

def countdown(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    while total_seconds:
        mins, sec = divmod(total_seconds, 60)
        hours = mins // 60
        mins = mins % 60
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, sec)
        print(timer, end='\r', flush=True)
        time.sleep(1)
        total_seconds -= 1
    
    print('Timer abgelaufen!')

hours = int(input('Stunden: '))
minutes = int(input('Minuten: '))
seconds = int(input('Sekunden: '))

countdown(hours, minutes, seconds)
"""



