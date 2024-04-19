# Wyświetl listę liczb od 1 do 20, ale dla liczb podzielnych przez 3 wydrukuj "Fizz",
# a dla liczb podzielnych przez 5 wydrukuj "Buzz". Dla liczb podzielnych zarówno przez 3,
# jak i przez 5 wydrukuj "FizzBuzz".

for a in range(1,21):
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz", end=" ")
    elif a % 3 == 0:
        print("Fizz", end=" ")
    elif a % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(a, end=" ")
