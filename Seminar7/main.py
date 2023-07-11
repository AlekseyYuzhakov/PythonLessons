import os
from random import randint
from math import pi


def task1():
    trasformation = lambda x: x
    values = [1, 23, 42, "asdfg"]
    transformed_values = list(map(trasformation, values))
    if values == transformed_values:
        print("ok")
    else:
        print("fail")
    print(transformed_values)

    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def find_farthest_orbit(list_of_orbits):
    imax = 0
    for a, b in list_of_orbits:
        if a != b:
            s = pi * a * b
            if imax < s:
                imax = s
                imax_a = a
                imax_b = b
    return imax_a, imax_b


def task2():
    orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
    print(*find_farthest_orbit(orbits))
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def same_by(op, x):
    return list(filter(op, x)) == x


def task3():
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2 == 0, values):
        print("same")
    else:
        print("different")


print("Какую задачу смотрим: 1, 2, .... или введите 0 чтобы посмотреть все ")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))


if task_number == 1:
    task1()
elif task_number == 2:
    task2()
elif task_number == 3:
    task3()
else:
    task1()
    task2()
    task3()

# def same_by (func, array):
#     result_list = []
#     for i in range(len(array)):
#         result_list.append(func(array[i]))
#     result_set=set(result_list) 
#     if len(result_set)>1:
#         return False
#     else:
#         return True