import os
import random

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


def get_list(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(random.randint(min_value, max_value + 1))
        array.append(i)
    return array

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# my_list_2 = []
# for elem in my_list:
#     if elem not in my_list_2:
#         my_list_2.append(elem) 
# print(len(my_list_2))

# list_1 = [1, 2, 3, 3]
# num_list1 = set(list_1)
# count = len(num_list1)
# print(count)

def taks17():
    print(
        "Задача №17. Решение в группах Дан список чисел. Определите, сколько в нем встречается различных чисел. Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6"
    )
    array17 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите  максимальное значение ")),
    )
    print("Мы получили следующий список {} ".format(array17))
    print("Количество уникальных значений = ", len(set(array17)))


taks17()
input("Нажмите Enter что бы продолжить ")
os.system("cls")

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


def shift_value_in_array(some_array, shift_value):
    for i in range(shift_value):
        last_value = some_array.pop()
        some_array.insert(0, last_value)
    return some_array

def taks19():
    print(
        "Задача №19. Решение в группах Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число. Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]"
    )
    array19 = get_list(
        int(input("Укажите количество чиселе в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите  максимальное значение ")),
    )
    print("Исходный список {} ".format(array19))
    shift_value_in_array(array19, int(input("Укажите величину смещения ")))
    print("Итоговый список после смещния {} ".format(array19))


taks19()
input("Нажмите Enter что бы продолжить ")
os.system("cls")

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


def task21():
    print(
        'Задача №21. Решение в группах Напишите программу для печати всех уникальных значений в словаре. Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]'
    )
    collection = {
        "V": "S001",
        "V": "S002",
        "VI": "S001",
        "VI": "S005",
        "VII": "S005",
        "V": "S009",
        " VIII": "S007",
    }
    value_set = []
    for key, value in collection.items():
        print(key, value)
        value_set.append(value)
    print(set(value_set))


task21()
input("Нажмите Enter что бы продолжить ")
os.system("cls")

def count_max_left_to_right(some_array):
    count = 0
    for i in range(1, len(some_array)):
        if some_array[i] > some_array[i - 1]:
            count += 1
    return count

def task23():
    print(
        "Задача №23. Решение в группах Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)"
    )
    array23 = get_list(
        int(input("Укажите количество чиселе в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите  максимальное значение ")),
    )
    print("Получен следующий список {}".format(array23))
    print(
        "Количество пар элементов удовлетворяющих условию {} ".format(
            count_max_left_to_right(array23)
        )
    )

task23()
input("Нажмите Enter что бы продолжить ")
os.system("cls")

