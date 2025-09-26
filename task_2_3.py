anzahl = 1
wert1 = 0
wert2 = 0
wert3 = 0
max_wert = 0

wert1 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

wert2 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

wert3 = float(input("Wert " + str(anzahl) + ": "))
anzahl += 1

if wert1 > wert2 and wert1 > wert3:
    max_wert = wert1
elif wert2 > wert3:
    max_wert = wert2
else:
    max_wert = wert3

print("Der grösste Wert ist:", max_wert)
#Kompilierfehler bei Zeile: 16 
#Grund: Nach dem "and" wird nicht angegeben was grösser als wert3 sein soll.
#Korrektur: "wert1" einfügen.
#Kompilierfehler bei Zeile: 19
#Grund: Falls wert2 grösser als wert3 ist gibt es nichts aus.
#Korrektur: Man fügt ein elif ein dass dann etwas ausgibt wenn die anderen nicht korrekt waren und wert2 als "max_wert" festlegt!