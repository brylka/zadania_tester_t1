def witaj(imie):
    print(f"Witaj {imie}!")

def idz_umyj_rece(jak_brudne):
    print("Idę umyć ręce!")
    if jak_brudne == 'czyste':
        print('Po co przychodzisz do łazienki jak masz czyste ręce?')
    elif jak_brudne == 'lekko':
        print('Myję ręce mydłem zapachowym.')
    elif jak_brudne == 'bardzo':
        print('Myję ręce pastą bhp!')
    else:
        print("Sprecyzuj jak brudne masz ręce!")
        idz_umyj_rece(input("Jak brudne masz ręce? (czyste/lekko/bardzo): "))

#witaj(input("Podaj swoje imię: "))

idz_umyj_rece(input("Jak brudne masz ręce? (czyste/lekko/bardzo): "))