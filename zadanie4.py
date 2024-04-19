# Wpisz słowo i sprawdź, czy jest ono dłuższe niż 5 liter.
# Jeśli tak, wyświetl "Długie słowo!", w przeciwnym razie "Krótkie słowo!".

slowo = input("Podaj słowo: ")

if len(slowo) > 5:
    print("Długie słowo!")
else:
    print("Krótkie słowo!")