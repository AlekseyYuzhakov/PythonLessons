import os


def A_in_pow_of_B(number, pow):
    while pow > 1:
        return number * A_in_pow_of_B(number, pow - 1)
    return number


def task26():
    print(
        "Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.*Пример:*A = 3; B = 5 -> 243 (3⁵)    A = 2; B = 3 -> 8 "
    )
    number_from_user = int(input("Введите число "))
    pow_from_user = int(input("Введите степень "))
    print(
        f"Число {number_from_user} в степени {pow_from_user} равно {A_in_pow_of_B(number_from_user,pow_from_user)}"
    )
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def sum_a_b(first_number, second_number):
    if first_number > second_number:
        first_number, second_number = second_number, first_number
    if first_number == 0:
        return second_number
    return sum_a_b(first_number - 1, second_number + 1)


def task28():
    print(
        "Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.*Пример:*2 2    4 "
    )
    first_number_from_user = int(input("Введите число "))
    second_number_from_user = int(input("Введите число "))
    print(
        f"Сумма двух чиссел {first_number_from_user} и {second_number_from_user} равна {sum_a_b(first_number_from_user, second_number_from_user)}"
    )


print("Какую задачу смотрим: 1, 2, или введите 0 чтобы посмотреть все ")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))


if task_number == 1:
    task26()
elif task_number == 2:
    task28()
else:
    task26()
    task28()
