# Wyświetl wszystkie parzyste liczby od 2 do 20.

for a in range(2,21):
    if a % 2 == 0:
        print(a, end=" ")
print()

for a in range(2,21,2):
    print(a, end=" ")