# Wydrukuj piramidę z gwiazdek o wysokości podanej przez użytkownika.

h = int(input("Podaj wysokość: "))

for a in range(1, 2 * h + 1, 2):
    print(' ' * (h - int(a/2)), "*" * a)