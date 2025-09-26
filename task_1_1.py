#block 1 Aufgabe 1

name = input("Bitte geben Sie Ihren Namen ein: ")
print("Guten Tag " + name + "!")
num = input("Bitte geben Sie zwei Zahlen ein, die sie addieren möchten (getrennt durch ein Leerzeichen): ")
num1, num2 = num.split()
summe = int(num1) + int(num2)
print(str(summe))