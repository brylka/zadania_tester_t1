# Sprawdź, czy lista ['Python', 'Java', 'C#', 'JavaScript'] zawiera język 'Python'.
# Jeśli tak, wydrukuj "Python jest na liście!", w przeciwnym razie "Brak Pythona na liście!".

lista = ['Python', 'Java', 'C#', 'JavaScript']

jest = False
for element in lista:
    if element == 'Python':
        jest = True
if jest:
    print("Python jest na liście!")
else:
    print("Brak Pythona na liście!")



if 'Python' in lista:
    print("Python jest na liście!")
else:
    print("Brak Pythona na liście!")
