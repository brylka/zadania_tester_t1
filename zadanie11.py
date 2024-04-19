# Napisz program, który zapyta użytkownika o cenę trzech produktów,
# a następnie obliczy i wydrukuje całkowity koszt zakupów.

cena1 = float(input("Podaj cenę produktu: "))
cena2 = float(input("Podaj cenę produktu: "))
cena3 = float(input("Podaj cenę produktu: "))

suma = cena1 + cena2 + cena3

print(f"Cena zakupów: {suma}")

suma = 0
for _ in range(3):
    suma += float(input("Podaj cenę produktu: "))
print(f"Cena zakupów: {suma}")