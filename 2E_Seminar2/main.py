a = int(input("Введите высоту елки "))

if isinstance(a, int):
    j = 1
    for i in range(a):
        print(" " * (a - i - 1) + "*" * j)
        j += 2
