import os


def find_vowel_in_string(some_string):
    vowel_max = ""
    max_count = 0
    for i in some_string:
        count = some_string.count(i)
        if count > max_count:
            max_count = count
            vowel_max = i
    return vowel_max


def find_rithm_in_string(some_string):
    vowel = find_vowel_in_string(some_string.replace("-", "").replace(" ", ""))
    separate_string = some_string.split()
    match_rithm = separate_string[0].count(vowel)
    for i in range(1, len(separate_string)):
        separate_string[i].replace("-", "")
        if separate_string[i].count(vowel) != match_rithm:
            return False
    return True


def task34():
    print(
        "Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке"
    )
    example_string = "пара-ра-рам рам-пам-папам па-ра-па-да"
    print("Исходный текст ", example_string)
    if find_rithm_in_string(example_string):
        print("Парам пам-пам ")
    else:
        print("Пам парам ")

    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


if __name__ == "__main__":
    task34()


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_columns + 1):
        sting_values = ""
        temp_list = []
        for j in range(1, num_rows + 1):
            sting_values = str(operation(i, j)) + "\t"
            temp_list.append(sting_values)
        print(*temp_list)


def task36():
    print(
        "Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения."
    )
    print_operation_table(lambda x, y: x * y)
    input("Нажмите Enter что бы продолжить ")
    os.system("cls")


if __name__ == "__main__":
    task36()

# def print_operation_table_2(operation, num_rows=6, num_columns=6):
#     numbers = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in numbers:
#         print(*[f'{j:2}' for j in i])

# print_operation_table_2(lambda x, y: x * y)
