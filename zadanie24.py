# Wydrukuj listę wszystkich liczb naturalnych mniejszych od 10,
# które są jednocześnie wielokrotnościami 2 lub 3.

for a in range(1,10):
    if a % 2 == 0 or a % 3 == 0:
        print(a, end=" ")