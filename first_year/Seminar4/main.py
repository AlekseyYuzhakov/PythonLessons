import os
import random
import time
from sys import getsizeof

print("Какую задачу смотрим: 1, 2, 3, 4, или все")
task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

if task_number == 1 or task_number >= 5:
    print(
        "Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. Input: a a a b c a a d c d d Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"
    )
    start = time.time()
    string = "a a a b c a a d c d d ".split()
    print(string)
    answer = ""
    my_dict = {}
    # new_list = []
    # for elem in string:
    #     if elem in new_list:
    #         answer += elem + "_" + str(new_list.count(elem)) + " "
    #     else:
    #         answer += elem + " "
    #     new_list.append(elem)
    # print(answer)
    for elem in string:
        if elem in my_dict:
            answer += elem + "_" + str(my_dict[elem]) + " "
            my_dict[elem] += 1
        else:
            answer += elem + " "
            my_dict[elem] = 1
    print(answer)
    print(my_dict)
    print(getsizeof(my_dict))
    print(getsizeof(answer))
    finish = time.time()
    print("Время работы алгоритма ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


if task_number == 2 or task_number >= 5:
    print(
        "Задача №27. Решение в группах Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте. Input: She sells sea shells on the sea shore The shells that she sells are sea shells Im sure. So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells Output: 13"
    )
    start = time.time()
    task_text = "She sells sea shells on the sea shore The shells that she sells are sea shells Im sure . So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells".lower().split()
    user_text = str(input("Введите текст ")).lower().split()
    user_text = task_text
    print(user_text)
    new_dict = {}
    for elem in user_text:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    for k in new_dict:
        if new_dict[k] == max(new_dict.values()):
            print("Самое повторяющиеся слово {} {} раз ".format(k, new_dict[k]))
    print(new_dict)
    print(len(new_dict))
    finish = time.time()
    print("Время работы алгоритма ", finish - start)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


#     text_user = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower().split(" ")
# set_1 = set(text_user)
# print(len(set_1))
# my_dict = {}
# for elem in text_user:
#     if elem in my_dict:
#         my_dict[elem] += 1
#     else:
#         my_dict[elem] = 1
# print(my_dict)
# for k,v in my_dict.items():
#     if v == max(my_dict.values()):
#         print ('{} встречается {} раз '.format(k, v))
