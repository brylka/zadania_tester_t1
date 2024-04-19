# Wydrukuj "Tak", jeśli bieżący rok jest rokiem przestępnym, w przeciwnym razie "Nie".

rok = int(input("Podaj rok: "))

if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
    print("Tak")
else:
    print("Nie")