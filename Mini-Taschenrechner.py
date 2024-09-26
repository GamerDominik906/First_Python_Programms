

print("Hallo Willkommen zu meinem Mini-Taschenrechner ")
print("")
operator= input ("Wähle zwischen + - * oder /. ")

zahl1 = float(input("Wähle die erste Zahl aus"))
zahl2 = float(input("Wähle die zweite Zahl aus"))

if operator == '+':
    ergebnis = zahl1 + zahl2
elif operator == '-':
    ergebnis = zahl1 - zahl2
elif operator == '*':
    ergebnis = zahl1 * zahl2
elif operator == '/':
    ergbnis = zahl1 / zahl2

else:
    print("Das ist ein ungültiger Operator")



print(f"Das ergebnis ist {ergebnis}")



