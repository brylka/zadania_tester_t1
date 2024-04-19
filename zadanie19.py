# Zapytaj użytkownika o temperaturę w stopniach Celsiusza i przelicz ją na stopnie Fahrenheit. Wydrukuj wynik.

c = float(input("Podaj temp w cel: "))

f = c * 1.8 + 32

print(f"{c}'C = {f}'F")