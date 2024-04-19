# Dla podanej listy owoców ['jabłko', 'banan', 'mango', 'kiwi'], znajdź najdłuższe słowo i wydrukuj je.

lista = ['jabłko', 'banan', 'mango', 'kiwi']

dlugosc_max = 0
slowo_max = ''

for element in lista:
    if dlugosc_max < len(element):
        dlugosc_max = len(element)
        slowo_max = element

print(f"Najdłuższe słowo to {slowo_max} ma {dlugosc_max} znaków.")

print(max(lista, key=len))