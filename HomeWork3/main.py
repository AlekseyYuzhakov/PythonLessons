import os
import random


def get_list(number, min_value, max_value):
    array = []
    for i in range(number):
        i = int(random.randint(min_value, max_value))
        array.append(i)
    return array


def find_n_in_array(some_array, number):
    count = 0
    for i in some_array:
        if i == number:
            count += 1
    return count


print("Какую задачу смотрим: 1, 2, 3, или введите 0 чтобы посмотреть все ")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

if task_number == 1 or task_number == 0:
    print(
        "Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X *Пример:* 5    1 2 3 4 5    3    -> 1"
    )
    list_task_16 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")),
    )
    print("Получен следующий список чисел {} ".format(list_task_16))
    print(
        "В списке есть следющиее количество совподающих элементов: ",
        find_n_in_array(list_task_16, int(input("Введите искомое значение "))),
    )
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


def find_closest_to_n_in_array(some_array, number):
    i_min_dif = 0
    min_dif = 10**10
    for i in range(len(some_array)):
        if some_array[i] > number:
            if min_dif > some_array[i] - number:
                min_dif = some_array[i] - number
                i_min_dif = i
        else:
            if min_dif > number - some_array[i]:
                min_dif = number - some_array[i]
                i_min_dif = i
    return some_array[i_min_dif]


if task_number == 2 or task_number == 0:
    print(
        "Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X *Пример:* 5     1 2 3 4 5     6     -> 5"
    )
    list_task_18 = get_list(
        int(input("Укажите количество чисел в списке ")),
        int(input("Укажите минимальное значение ")),
        int(input("Укажите максимальное значение ")),
    )
    print("Получен следующий список чисел {} ".format(list_task_18))
    print(
        "Ближайший элемент к искомому значению ",
        find_closest_to_n_in_array(
            list_task_18, int(input("Введите искомое значение "))
        ),
    )
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")

if task_number == 3 or task_number == 0:
    print(
        "Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы. *Пример:* ноутбук 12"
    )
    english_dict = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "S": 1,
        "T": 1,
        "R": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10,
    }
    user_word = list(str(input("input your word ")).upper())
    print(user_word)
    symbol_points = 0
    for elem in user_word:
        if elem in english_dict:
            symbol_points += english_dict[elem]    
    print('Количество очков равно ',symbol_points)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")
