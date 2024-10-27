def task1():
    a = 1
    b = 1
    c = 5

    if a > b + c or b > a + c or c > a + b:

        print("Треугольник не существует ")

    else:
        if (a + b + c) / 3 == a:
            print("Треугольник существует\n" + "Треугольник равносторонний\n")
        elif (a + b) / 2 == a or (b + c) / 2 == b or (c + a) / 2 == c:
            print("Треугольник существует\n" + "Треугольник равнобедренный\n")
        else:
            print("Треугольник существует\n" + "Треугольник разносторонний\n")


def task2():
    num = 2

    if num == 2:
        print("Простое")
    elif 1 < num < 100000:
        step = 3
        if num % 2 != 0:
            while step < num:
                if num % step == 0:
                    print("Не является простым")
                    break
                step += 2
        else:
            print("Не является простым")
        if step == num:
            print("Простое")
    else:
        print("Число должно быть больше 1 и меньше 100000")


def task3():
    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    counter = 0
    for item in list1:
        if item in list2:
            counter += 1
    print("Количество совпадающих чисел: ", counter)


task3()
