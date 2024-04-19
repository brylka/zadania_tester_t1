# Napisz funkcję, która przyjmie listę liczb i zwróci tylko te elementy,
# które są większe od średniej wszystkich liczb w liście.

lista=[1,2,3,4,5]

suma = 0
for a in lista:
    suma += a

srednia = suma/len(lista)

lista_druga = []
for a in lista:
    if a > srednia:
        lista_druga.append(a)

print(lista_druga)