
import json
import math
import random as rnd
import csv
from typing import Callable

file_name = "new_file.csv"


def save_to_json(func: Callable):
    def wraper(*args, **kwargs):
        with open(args[0], "r", encoding="UTF-8", newline="") as csv_file:
            all_data = []
            csv_reader = csv.reader(csv_file, dialect="excel")
            for row in csv_reader:
                for line in row:
                    tem_dic = {}
                    if not len(line) == 0:
                        #print(line)
                        line = line.strip().replace("[", "").replace("]", "").split(",")
                        tem_dic.setdefault(
                            "parameters", f"{(line[0], line[1], line[1])}"
                        )
                        tem_dic.setdefault(
                            "result", f"{func(int(line[0]),int(line[1]),int(line[2]))}"
                        )
                    all_data.append(tem_dic)
            #print(all_data)
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

    return #print(f"Создан CSV файл с именем {file_name} содержащий {rows} строк ")


generate_csv_file(file_name, 10)
find_roots(file_name)
