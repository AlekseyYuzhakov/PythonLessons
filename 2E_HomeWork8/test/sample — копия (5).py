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


def traverse_directory(directory: str = os.getcwd()):
    file_list = []
    dir_list = []
    for dir_path, dir_names, file_names in os.walk(directory):
        for file in file_names:
            temp_file_dict = {}
            file_path = os.path.join(dir_path, file)
            file_size = os.path.getsize(file_path)
            fpath = Path(file_path)
            temp_file_dict.setdefault("Path", file_path)
            temp_file_dict.setdefault("Type", "File")
            temp_file_dict.setdefault("Size", file_size)
            if fpath.parent.name:
                temp_file_dict.setdefault("Parent", fpath.parent.name)
            file_list.append(temp_file_dict)
        if dir_names:
            for dir in dir_names:
                temp_dir_dict = {}
                dir_path = os.path.join(dir_path, dir)
                dir_size = os.path.getsize(dir_path)
                dpath = Path(file_path)
                temp_dir_dict.setdefault("Path", dir_path)
                temp_dir_dict.setdefault("Type", "Directory")
                temp_dir_dict.setdefault("Size", dir_size)
                if dpath.parent.name:
                    temp_dir_dict.setdefault("Parent", fpath.parent.name)
                dir_list.append(temp_dir_dict)
    print(file_list)
    print(dir_list)
    return file_list + dir_list


def save_results_to_json():
    pass


def save_results_to_csv():
    pass


def save_results_to_pickle():
    pass


traverse_directory("D:\\GBru\\Учеба\\Enter_python\\Code\\PythonLessons\\2E_HomeWork7")
