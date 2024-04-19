#Przyjmij liczbę od użytkownika i wyświetl "Liczba dodatnia", jeśli liczba jest większa od 0,
# "Liczba ujemna", jeśli jest mniejsza od 0, lub "Zero", jeśli jest równa 0.

a = int(input("Podaj liczbę: "))

#print(type(a))

if a > 0:
    print("Liczba dodatnia")
elif a < 0:
    print("Liczba ujemna")
elif a == 0:
    print("Zero")