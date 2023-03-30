""" ZAHLEN-RATE-SPIEL

a) Schreibe ein Programm, welches den Nutzer die geheime
   Zahl des Computers (Ganzzahl zwischen 1 und 10) erraten lässt.
   - Der Nutzer hat bis zu 2 Versuche
   - Sollte er es im ersten Versuch schaffen, kommt es
     nicht zu einem zweiten Versuch
   - Sollte er es im ersten Versuch nicht schaffen, hat
     er im zweiten eine weitere Chance

bonus) Gebe dem Nutzer Tipps, ob er zu hoch oder zu 
       niedrig geraten hat.
"""
import random

# EINGABE
bot_nr = random.randint(1, 10) # zufälliger int zw. 1 und 10

# VERARBEITUNG

# AUSGABE