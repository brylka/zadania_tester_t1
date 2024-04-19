# Wyświetl liczby od 0 do 10 z separatorem pomiędzy liczbami znakiem &.

for a in range(11):
    if a < 10:
        print(a, end="&")
    else:
        print(a)

for a in range(10):
    print(a, end="&")
print(10)