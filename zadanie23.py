# Przyjmij od użytkownika liczbę i sprawdź, czy jest ona liczbą pierwszą

a = int(input("Podaj liczbę: "))

prime = True
if a > 1:
    for i in range(2,a):
        if a % i == 0:
            prime = False
            break
else:
    prime = False

if prime:
    print(f"Liczba {a} jest pierwsza")
else:
    print(f"Liczba {a} nie jest pierwsza")