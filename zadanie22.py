# Napisz program, który wyświetli pierwszych 10 liczb ciągu Fibonacciego.

a,b = 0,1
print(a, b, end=" ")
for _ in range(8):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

