"""
Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
"""

import json
import math
import random as rnd
import csv
from typing import Callable

file_name = (
    "D:\\GBru\\Учеба\\Enter_python\\Code\\PythonLessons\\2E_HomeWork9\\new_file.csv"
)


def save_to_json(func: Callable):
    def wraper(*args, **kwargs):
        with open(args[0], "r", encoding="UTF-8", newline="") as csv_file:
            all_data = []
            csv_reader = csv.reader(csv_file, dialect="excel")
            for row in csv_reader:
                for line in row:
                    tem_dic = {}
                    if not len(line) == 0:
                        print(line)
                        line = line.strip().replace("[", "").replace("]", "").split(",")
                        tem_dic.setdefault(
                            "parameters", f"{(line[0], line[1], line[1])}"
                        )
                        tem_dic.setdefault(
                            "result", f"{func(int(line[0]),int(line[1]),int(line[2]))}"
                        )
                    all_data.append(tem_dic)
            print(all_data)
        with open("results.json", "w", encoding="UTF-8") as json_file:
            json.dump(all_data, json_file, ensure_ascii=False)

    return wraper


@save_to_json
def find_roots(a=0, b=0, c=0):
    discr = b**2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return (x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        return x
    return None


def generate_csv_file(file_name="new_file.csv", rows=3):
    temp_list = []
    with open(file_name, "w", encoding="UTF-8") as file:
        csv_writer = csv.writer(file, dialect="excel")
        for _ in range(rows):
            temp_row = []
            temp_row.append(rnd.randint(100, 1000))
            temp_row.append(rnd.randint(100, 1000))
            temp_row.append(rnd.randint(100, 1000))
            temp_list.append(temp_row)
        csv_writer.writerow(temp_list)

    return print(f"Создан CSV файл с именем {file_name} содержащий {rows} строк ")


generate_csv_file(file_name, 10)
find_roots("new_file.csv")
