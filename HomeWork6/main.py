import os
import random


def find_n_arg_in_arithmetic_progression(start, n, shift, list_progress):
    if len(list_progress) > n:
        return start + (n - 1) * shift
    return "отсутствует в списке"


def task30():
    print(
        "Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки."
    )
    statr_number = int(input("Укажите первый элемент прогрессии "))
    finish_number = int(input("Укажите количество элементов прогрессии "))
    step_size = int(input("Укажите шаг "))
    list_task_30 = [i for i in range(statr_number, finish_number, step_size)]
    counter = 0
    for i in list_task_30:
        counter += 1
        print(f"№ {counter} = {i} ")
    # print(*list_task_30, sep="\n") "Как вариант"
    serched_n_in_prog = int(input("Укажите искомый 'n' элемент прогрессии  "))
    print(
        f'Искоммый "n" элемент прогрессии {find_n_arg_in_arithmetic_progression(statr_number, serched_n_in_prog, step_size,list_task_30)}'
    )
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def find_valuses_pos_in_range(some_list, min_wall, max_wall):
    new_list = []
    for i in range(len(some_list)):
        if min_wall <= some_list[i] <= max_wall:
            new_list.append(i)
    return new_list


def task32():
    print(
        "Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)"
    )
    min_values = int(input("Укажите минимальное значение в списке "))
    max_values = int(input("Укажите максимальное значение в списке "))
    list_task_32 = [
        random.randint(min_values, max_values)
        for i in range(int(input("Укажите длинну списка ")))
    ]
    print(f"Получен следующий список {list_task_32} ")
    list_task_32_positions = find_valuses_pos_in_range(
        list_task_32,
        int(input("Укажите нижнюю границу диапозона ")),
        int(input("Укажите верхнюю границу диапозона ")),
    )
    print(f"Значения с индексами {list_task_32_positions} соответсвуют диапозону ")
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


print("Какую задачу смотрим: 1, 2, или введите 0 чтобы посмотреть все ")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

if task_number == 1:
    task30()
elif task_number == 2:
    task32()
else:
    task30()
    task32()
