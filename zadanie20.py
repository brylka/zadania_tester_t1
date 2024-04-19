# Napisz program, który dla podanej listy liczb znajdzie minimum
# i maksimum bez używania wbudowanych funkcji min() i max().

lista = [43,2,54,2,23,-76,12]

maximum = lista[0]
minimum = lista[0]

for element in lista:
    if element < minimum:
        minimum = element
    if element > maximum:
        maximum = element

print(f"Maksimum {maximum} minimum {minimum}")