from os import system
from random import randint
import time


print(
    "Какую задачу смотрим: введите порядковый номер задачи или введите 0 чтобы посмотреть все"
)
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))


def get_list_from_user(number):
    array = []
    for i in range(number):
        array.append(int(input("Введите число ")))
    return array


def get_list(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(randint(min_value, max_value))
        array.append(i)
    return array


if task_number == 1 or task_number == 0:
    print(
        "Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива Ввод: Вывод: 7 3 3 2 12 3 1 3 4 2 4 12 6 4 15 43 1 15 1 (каждое число вводится с новой строки)"
    )
    start = time.time()
    list_task_39a = get_list_from_user(
        int(input("Укажите количество элементов в списке "))
    )
    print("Первый список ", list_task_39a)
    list_task_39b = get_list_from_user(
        int(input("Укажите количество элементов в списке "))
    )
    print("Второй список ", list_task_39b)
    for i in list_task_39a:
        if i not in list_task_39b:
            print(i)

    finish = time.time()
    print("Время работы программы ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    system("cls")

if task_number == 2 or task_number == 0:
    print(
        "Задача №41. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. Ввод: Ввод: 5 5 1 2 3 4 5 1 5 1 5 1 Вывод: Вывод: 0 2 "
    )
    list_task_41 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")),
    )
    print("Получен следующий список ", list_task_41)
    start = time.time()
    count_serched_number_req = 0
    for i in range(1, len(list_task_41) - 1):
        if list_task_41[i - 1] < list_task_41[i] > list_task_41[i + 1]:
            count_serched_number_req += 1
    print("Количество элементов удовлетворяюих условию = ", count_serched_number_req)
    finish = time.time()
    print("Время работы программы ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    system("cls")

if task_number == 3 or task_number == 0:
    print(
        " Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках. Ввод: Вывод: 1 2 3 2 3 2 "
    )
    list_task_43 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")),
    )
    print(list_task_43)
    count = 0
    for i in range(len(list_task_43) - 1):
        for j in range(i + 1, len(list_task_43)):
            if list_task_43[i] == list_task_43[j]:
                count += 1
    print("Количество элементов удовлетворяющих условию ", count)
    input("Нажмите Enter что бы продолжить ")
    system("cls")


if task_number == 4 or task_number == 0:
    print(
        " Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105 . Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). Ввод: Вывод: 300 220 284"
    )
    k_range = int(input("Введите диапозон "))
    for first_number in range(1, k_range):
        for second_number in range(first_number + 1, k_range):
            i = 1
            j = 1
            sum_div1 = 0
            sum_div2 = 0
            while i < first_number:
                if first_number % i == 0:
                    sum_div1 += i
                i += 1
            while j < second_number:
                if second_number % j == 0:
                    sum_div2 += j
                j += 1
            if sum_div1 == second_number and sum_div2 == first_number:
                print(f"Пара чисел {first_number} и {second_number}")
    input("Нажмите Enter что бы продолжить ")
    system("cls")
