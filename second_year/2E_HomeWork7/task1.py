import os

source_path = "test_folder"
desired_name = "sample"
num_digits = 3
source_ext = ".txt"
target_ext = ".bmp"
origin_name_range = None

# ".bmp"
# ".txt"


def rename_files(desired_name, num_digits, source_ext, target_ext, origin_name_range):
    count = 0
    os.chdir("2E_HomeWork7/test_folder")
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        res_name = ""
        print(f"{dir_path= }\n{dir_name= }\n{file_name= }")
        for file in file_name:
            res_name = ""
            if file.count(source_ext):
                res_name = file.replace(source_ext, "")
                if origin_name_range != None:
                    res_name = res_name[origin_name_range[0] : origin_name_range[1] :]
                res_name = res_name + desired_name + "0" * num_digits + str(count)
                if target_ext != source_ext:
                    res_name = res_name + target_ext
                else:
                    res_name = res_name + source_ext
                count += 1
                os.rename(str(file), str(res_name))


rename_files(desired_name, num_digits, source_ext, target_ext, origin_name_range)


# import os

# def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
#     new_names = []

#     # Получаем список файлов в текущей директории
#     files = os.listdir('test_folder')

#     # Фильтруем только нужные файлы с указанным расширением
#     filtered_files = [file for file in files if file.endswith(source_ext)]

#     # Сортируем файлы по имени
#     filtered_files.sort()

#     # Задаем начальный номер для порядкового номера
#     num = 1

#     # Переименовываем файлы
#     for file in filtered_files:
#         # Получаем имя файла без расширения
#         name = os.path.splitext(file)[0]

#         # Если задан диапазон, обрезаем имя файла
#         if name_range:
#             name = name[name_range[0]-1:name_range[1]]

#         # Создаем новое имя с желаемым именем, порядковым номером и новым расширением
#         new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext

#         # Переименовываем файл
#         path_old = os.path.join(os.getcwd(), folder_name, file)
#         path_new = os.path.join(os.getcwd(), folder_name, new_name)
#         os.rename(path_old, path_new)

#         # Увеличиваем порядковый номер
#         num += 1