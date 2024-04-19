# Utwórz prosty kalkulator, który zapyta użytkownika o dwi liczby oraz operację
# (dodawanie, odejmowanie, mnożenie, dzielenie) do wykonania, a następnie wyświetli wynik.

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
operacja = input("Wybierz działanie (+ - * /)")

if operacja == '+':
    print(f"{a}+{b}={a+b:.4f}")
elif operacja == '-':
    print(f"{a}-{b}={a-b:.4f}")
elif operacja == '*':
    print(f"{a}*{b}={a*b:.4f}")
elif operacja == '/':
    if b != 0:
        print(f"{a}/{b}={a/b:.4f}")
    else:
        print("Nie dzieli sie przez zero.")