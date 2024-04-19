# Utwórz listę zawierającą tylko parzyste elementy z listy liczb [1, 2, 3, 4, 5, 6].

lista = [1, 2, 3, 4, 5, 6]
parzyste = []

for element in lista:
    if element % 2 == 0:
        parzyste.append(element)

print(parzyste)
