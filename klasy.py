class Osoba:
    def __init__(self, xxx, yyy):
        self.imie = xxx
        self.wiek = yyy
    def przedstaw_sie(self):
        print(f"Nazywam sie {self.imie}!")
    def ile_masz_lat(self):
        print(f"Mam lat {self.wiek}.")

#Osoba().przedstaw_sie()

bartosz = Osoba("Bartosz", 45)
bartosz.przedstaw_sie()
bartosz.ile_masz_lat()

pawel = Osoba("Paweł", 30)
pawel.przedstaw_sie()
pawel.ile_masz_lat()