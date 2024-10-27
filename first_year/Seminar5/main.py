import os
import random
import time

print(
    "Какую задачу смотрим: введите порядковый номер задачи или введите 0 чтобы посмотреть все"
)
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))


def get_list(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(random.randint(min_value, max_value))
        array.append(i)
    return array


def fibonachi_number(integer):
    if integer in (1, 2):
        return 1
    return fibonachi_number(integer - 1) + fibonachi_number(integer - 2)


if task_number == 1 or task_number == 0:
    print(
        "Задача №31. Решение в группах Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1  = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи Input: 7 Output: 21 Задание необходимо решать через рекурсию "
    )
    start = time.time()
    print(f' {fibonachi_number(int(input("Введите число ")))}')
    finish = time.time()
    print("Время работы программы ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def vasily_haker_fail_check(some_array):
    for i in range(len(some_array)):
        if some_array[i] == max(some_array):
            some_array[i] = min(some_array)
    return some_array


if task_number == 2 or task_number == 0:
    print(
        "Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на инимальные. Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1"
    )
    grades_count = int(input("Сколько оценок в журнале "))
    grades_in_jurnal = [random.randint(1, 5) for i in range(grades_count)]
    start = time.time()
    print("Следующие оценки стоят в журнале ", grades_in_jurnal)
    print(vasily_haker_fail_check(grades_in_jurnal))
    finish = time.time()
    print("Время работы программы ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def prime_number_check(number):
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


if task_number == 3 or task_number == 0:
    print(
        "Задача №35. Решение в группах Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число) Input: 5 Output: yes"
    )
    print(prime_number_check(int(input("Введите целое число "))))
