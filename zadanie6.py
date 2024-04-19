# Sprawdź, czy podane słowo kończy się literą 'a'.
# Jeśli tak, wyświetl "Kończy się na 'a'!", w przeciwnym razie "Nie kończy się na 'a'!".
#        0123456789
slowo = 'Pythonsda'

#if slowo[len(slowo)-1] == 'a':
if slowo[-1] == 'a':
    print("Kończy się na 'a'!")
else:
    print("Nie kończy się na 'a'!")
