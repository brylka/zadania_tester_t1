# Dla liczby podanej przez użytkownika, wydrukuj "Dziwna liczba",
# jeśli liczba jest nieparzysta lub parzysta ale w zakresie od 6 do 20 włącznie.
# W przeciwnym razie wydrukuj "Zwykła liczba".

a = int(input("Podaj liczbę: "))

if a % 2 != 0 or (a % 2 == 0 and a >= 6 and a <= 20):
    print("Dziwna liczba")
else:
    print("Zwykła liczba")