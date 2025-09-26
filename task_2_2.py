anzahl = 0
note1 = 0.0
note2 = 0.0
note1 = float(input("Note 1:"))
anzahl += 1
note2 = float(input("Note 2:"))
anzahl += 1
schnitt = (note1 + note2) / anzahl
if schnitt >= 4:
    print("*****")
    durchschnitt = int(schnitt * 2)
    durchschnitt = (durchschnitt + 1) // 2
    if durchschnitt == 4:
        print("Typ 2")
    else:
        if durchschnitt == 5:
            print("Typ 3")
        else:
            print("Typ 4")
else:
    print("-----")
    if note1 >= 4 or note2 >= 4:
        print("Typ 1")
    else:
        print("Typ 0")
#a) Die erste Bedinung stimmt nicht überein, da der Durchschnitt von 4.2 & 3.5 nicht grösser als 4 ist.
#   Bei der else Bedinung ist der erste Teil der Bedinung korrekt weil note1 grösser als 4 ist.
#   Sommit gibt a) "-----" & "Typ 1" aus!
#b) Die erste Bedinung stimmt überein, da der Durchschnitt von 5.2 & 5.8 mehr als 4 ist.
#   In der Bedinung stimmt der Durchschnitt jedoch mit keiner Bedinungen ausser dem letzten else Bedinung zu.
#   Sommit gibt b) "*****" & "Typ 4" aus!
#c) Die erste Bedinung stimmt nicht überein, da der Durchschnitt von 3.8 & 3.3 nicht grösser als 4 ist.
#   Bei der else Bedinung ist stimmt ist weder note1 noch note2 grösser als 4 und die else Bedinung ist übrig.
#   Sommit gibt c) "-----" & "Typ 0" aus!