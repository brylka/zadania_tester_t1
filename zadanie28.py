# Sprawdź, czy podany przez użytkownika ciąg znaków zawiera co najmniej jedną cyfrę.

ciag = input("Podaj ciąg znaków: ")

cyfry = ['0','1','2','3','4','5','6','7','8','9']
for znak in ciag:
    if znak in cyfry:
        print(f"Ciąg znaków: {ciag} zawiera cyfrę.")
    else:
        print(f"Ciąg znaków: {ciag} NIE zawiera cyfrę.")

