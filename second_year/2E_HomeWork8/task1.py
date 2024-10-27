"""
Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории. Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория. Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. 
Важные детали:

Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей. После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.

Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий. При этом сначала добавляются файлы, а затем директории.

Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), и затем получается размер файла (size = os.path.getsize(path)). Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.

Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)), и вызывается функция get_dir_size(path), чтобы получить размер всей директории с учетом ее содержимого. Информация о директории добавляется в список results в виде словаря {'Path': path, 'Type': 'Directory', 'Size': size}.
"""

import os
from pathlib import Path
import json
import csv
import pickle


def traverse_directory(directory: str = os.getcwd()):
    file_list = []
    dir_list = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file in file_names:
            temp_file_dict = {}
            file_path = os.path.join(dir_path, file)
            file_size = os.path.getsize(file_path)
            temp_file_dict.setdefault("Path", file_path)
            temp_file_dict.setdefault("Type", "File")
            temp_file_dict.setdefault("Size", file_size)
            file_list.append(temp_file_dict)
        if dir_names:
            for dir in dir_names:
                temp_dir_dict = {}
                dir_path = os.path.join(dir_path, dir)
                dir_size = folderSize(dir_path)
                temp_dir_dict.setdefault("Path", dir_path)
                temp_dir_dict.setdefault("Type", "Directory")
                temp_dir_dict.setdefault("Size", dir_size)
                dir_list.append(temp_dir_dict)
    return file_list + dir_list


def folderSize(path):
    fsize = 0
    for file in Path(path).rglob("*"):
        if os.path.isfile(file):
            fsize += os.path.getsize(file)
    return fsize


def save_results_to_json(results, name="save_results_to_json"):
    with open(name, "a", newline="", encoding="UTF-8") as file:
        for dict in results:
            json.dump(dict, file, ensure_ascii=False)


def save_results_to_csv(results, name="save_results_to_csv"):
    with open(name, "a", encoding="UTF-8") as file:
        csv_write = csv.writer(file, dialect="excel")
        all_data = []
        all_data.append(results[0].keys())
        for _dict in results:
            all_data.append(_dict.values())
        csv_write.writerows(all_data)


def save_results_to_pickle(results, name="save_results_to_pickle.pkl"):
    with open(name, "ab") as file:
        for _dict in results:
            pickle.dump(_dict, file)


results = traverse_directory(
    "D:\\GBru\\Учеба\\Enter_python\\Code\\PythonLessons\\2E_HomeWork8"
)

save_results_to_json(results)
# save_results_to_csv(results)
# save_results_to_pickle(results)
print(results)


"""
import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)

    return total_size

def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results

def save_results_to_json(results, file_path):
    with open(file_path, 'w') as file:
        json.dump(results, file)

def save_results_to_csv(results, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(results, file)
"""
