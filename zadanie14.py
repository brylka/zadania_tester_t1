# Napisz program, który obliczy średnią z trzech podanych przez użytkownika liczb.

suma = 0
for _ in range(3):
    suma += float(input("Podaj liczbę: "))

print(f"Średnia liczb wynosi {suma/3:.2f}")