# Zapytaj użytkownika o jego wiek i wydrukuj, ile lat minęło od osiągnięcia przez niego
# pełnoletności lub ile lat zostało do jej osiągnięcia.

a = int(input("Podaj swój wiek: "))

if a > 18:
    print(f"Minęły {a - 18} lata od osiągnięcia pełnoletności.")
elif a == 18:
    print(f"Osiągnąłeś pełnoletnośc właśnie.")
else:
    print(f"Do pełnoletności zostało {18 - a} lat.")