zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))
if zahl2 < zahl1 and zahl1 > 5:
    temp = zahl1
    zahl1 = zahl2
    zahl2 = temp
else:
    if zahl1 == zahl2:
        zahl1 = 5
    zahl2 = 8
print("Ausgabe 1 =", zahl1)
print("Ausgabe 2 =", zahl2)
#a) Die Zahlen erfüllen die if Bedinung und dadurch wird zuerst temp zu 6(zahl1) gesetzt,
#   dann wird zahl1 zu 3(zahl2) gesetzt & auch noch zahl2 zu 6(temp) gesetzt.
#   Die Ausgabe ist dann also "Ausgabe 1 = 3" & "Ausgabe 2 = 6"!
#b) Die Zahlen erfüllen zwar nicht die erste Bedinung, aber dahingegen die Bedinung im else,
#   weil die Zahlen gleich sind, wird dann zahl1 zu 5 gesetzt & zahl2 zu 8.
#   Die Ausgabe ist dann also "Ausgabe 1 = 5" & "Ausgabe 2 = 8"!