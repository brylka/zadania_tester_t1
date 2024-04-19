def sakamoto(d, m, y):
    # https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week
    t = [0,3,2,5,0,3,5,1,4,6,2,4]
    if m < 3:
        y -= 1
    result = (y + y//4 - y//100 + y//400 + t[m-1] + d) % 7
    print(result)
    return result if result != 0 else 7

def max_day(m, y):
    if m < 1 or m > 12:
        return False
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    elif m == 2:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 31

miesiac = int(input("Podaj miesiąc: "))
rok = int(input("Podaj rok: "))

#start = int(input("Dzień startowy: "))
#ilosc = int(input("Ilość dni w miesiącu: "))
start = sakamoto(1,miesiac, rok)
ilosc = max_day(miesiac, rok)

print("Pn Wt Śr Cz Pt \033[33mSo \033[31mNd\033[0m")

# Pętla drukująca puste miejsca - są to dni z poprzedniego miesiąca
# Jest to liczba startowa pomniejszona o jeden
for _ in range(start-1):
    print("  ", end=" ")
 #print(end=" x ")

# Pętla główna drukująca wszystkie dni danego miesiąca
for a in range(1,ilosc+1):
    if a < 10:
        print(end=" ")
    if (a + start - 1) % 7 == 0:
        print("\033[31m", a, "\033[0m", sep="", end=" ")
    elif (a + start - 1) % 7 == 6:
        print("\033[33m", a, "\033[0m", sep="", end=" ")
    else:
        print(a, end=" ")

    # Warunek wprawdzający czy jest 7 dni w rzędzie z uwzględnieniem startu
    if (a + start - 1) % 7 == 0:
        print()