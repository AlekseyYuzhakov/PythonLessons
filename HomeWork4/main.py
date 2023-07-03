import os
import random


def get_list_random(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(random.randint(min_value, max_value))
        array.append(i)
    return array


def get_list_from_user(number):
    array = []
    for i in range(number):
        array.append(int(input("Введите число ")))
    return array


def merge_list_by_same_values(first_array, second_array):
    result_array = []
    for i in range(len(first_array)):
        for j in range(len(second_array)):
            if first_array[i] == second_array[j]:
                result_array.append(second_array[j])
    return result_array


print("Какую задачу смотрим: 1, 2, или введите 0 чтобы посмотреть все ")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

if task_number == 1 or task_number == 0:
    print(
        "Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."
    )
    list_task22a = get_list_from_user(int(input("Введите длинну первого списка ")))
    list_task22b = get_list_from_user(
        int(input("Введите длинну второго списка списка "))
    )
    merge_result = set(merge_list_by_same_values(list_task22a, list_task22b))
    print(
        "Оба списка содежат следующий набор совподающих значений ", sorted(merge_result)
    )
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def find_best_bush_with_berries(some_list):
    best_berries_count = 0
    for i in range(len(some_list)):
        if best_berries_count < (
            some_list[i] + some_list[i - 1] + some_list[(i + 1) % len(some_list)]
        ):
            best_berries_count = (
                some_list[i] + some_list[i - 1] + some_list[(i + 1) % len(some_list)]
            )
    return best_berries_count


if task_number == 2 or task_number == 0:
    print(
        "Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."
    )
    cherry_bush_berries_count_list = get_list_random(
        int(input("Укажите количество кустов на грядке ")),
        int(input("Укажите минимальное количество ягод на кусте ")),
        int(input("Укажите максимальное количество ягод на кусте ")),
    )
    print(
        "Кусты с ягодами расположены следующим образом ", cherry_bush_berries_count_list
    )
    print(
        "Лучший куст для сбора урожая ",
        find_best_bush_with_berries(cherry_bush_berries_count_list),
    )

    input("Нажмите Enter что бы продолжить ")
    os.system("cls")
