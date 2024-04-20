def dodaj(a,b):
    return a + b
    #c = a + b
    #return c

def odejmij(a,b):
    return a - b

def pomnoz(a,b):
    return a * b

def podziel(a,b):
    if b != 0:
        return a / b
    else:
        return "Nie dzieli się przez zero!"

#wynik = dodaj(10,20)
#print(wynik)

print(dodaj(10,20))
print(odejmij(20,30))
print(pomnoz(11,12))
print(podziel(10,3))
print(podziel(10,0))
