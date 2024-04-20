class Osoba:
    def __init__(self, xxx, yyy):
        self.imie = xxx
        self.wiek = yyy
    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie}!")
    def ile_masz_lat(self):
        print(f"Mam lat {self.wiek}.")
    def zmien_imie(self,zzz):
        self.imie = zzz
    def dodaj(self,a,b):
        print(f"Ja {self.imie} twierdzę, że: {a} + {b} = {a + b}")

class Test:
    def odejmij(self, c, d):
        return c - d
#Osoba().przedstaw_sie()

bartosz = Osoba("Bartosz", 45)
bartosz.przedstaw_sie()
bartosz.ile_masz_lat()

pawel = Osoba("Paweł", 30)
pawel.przedstaw_sie()
pawel.ile_masz_lat()

bartosz.zmien_imie("Aleksander")
bartosz.przedstaw_sie()
bartosz.dodaj(10,20)
pawel.dodaj(10,20)

print(Test().odejmij(30,20))