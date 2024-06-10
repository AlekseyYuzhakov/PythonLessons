import os


# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.


def print_phone_book(list_list):
    print("id   Фамилия Имя Отчество    Телефон")
    for elem in list_list:
        print(elem.strip().replace(";", " "))


def read_file(path):
    temp = []
    with open(path, "r", encoding="utf - 8") as f:
        for elem in f:
            temp.append(elem)
    return temp


def add_to_file(list_some):
    Id_user = input("Введите id ")
    name = input("Введите имя ")
    phone_number = input("Укажите номер телефона ")
    result_text = Id_user + ";" + name + ";" + phone_number + "\n"
    list_some.append(result_text)
    return list_some


def delete_number(some_list):
    ask_for_serch = input("Укажите Имя, Фамилию, или № телефона для поиска ")
    pos = 0
    for elem in some_list:
        if ask_for_serch in elem:
            print(f"{elem.replace(';',' ')} Удалить запись? ")
            if str(input("Yes or No ")).lower in ["y", "yes", "yep", "ye"]:
                some_list.pop(pos)
                print("Запись удалена ")
        pos += 1
    return some_list


def write_to_file_with_close(some_list):
    with open("phonebook.txt", "w", encoding="utf - 8") as f:
        for elem in some_list:
            f.writelines(elem)


phone_list = read_file("phonebook.txt")


def main(phone_list):
    while True:
        print()
        print(
            "Нажмите 1 если хотите посмотреть справочник\nНажмите 2 если хотете внести запись\nНажмите 3 если хотете удалить запись\nНажмите 0 что бы выйти из меню\n"
        )
        task_number = int(input())
        os.system("cls")
        if task_number == 1:
            print_phone_book(phone_list)
        elif task_number == 2:
            phone_list = add_to_file(phone_list)
        elif task_number == 3:
            phone_list = delete_number(phone_list)
        elif task_number == 0:
            write_to_file_with_close(phone_list)
            break


if __name__ == "__main__":
    main(phone_list)


# from tabulate import tabulate
# import csv


# def readfile(filename):
#     read_data = [i.strip().split(';') for i in open(filename, 'r', encoding='utf-8')]
#     # read_data = []
#     # with open('tel.txt', 'r', encoding='utf-8') as file:
#     #     for elem in file:
#     #         read_data.append(elem.split())
#     return read_data


# def menu():
#     print('===============================')
#     print('Выберите одно из действий:')
#     print('1 - вывести справочник на экран')
#     print('2 - произвести экпорт данных')
#     print('3 - поиск абонентов')
#     print('4 - удаление из справочника по id')
#     print('5 - добавление записи в справочник')
#     print('0 - выход из программы')


# def printinfo(data):
#     # print('id \t Фамилия Имя Отчество \t номер телефона')
#     # for elem in data:
#     #     print(*elem, sep='\t')
#     print(tabulate(data, headers=['id', 'ФИО', 'Телефон'], tablefmt='orgtbl'))

# def export_to_csv(data):
#     with open('example2.csv', 'w', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#     print('Экспорт завершён')


# def search(data):
#     what = input('Что ищем? ')
#     searched_data = []
#     for string in data:
#         for elem in string:
#             if (what in elem) and string not in searched_data:
#                 searched_data.append(string)
#     if searched_data:
#         printinfo(searched_data)
#     else:
#         print('Строки, удовлетворяющие условиям поиска, не найдены')


# def delete(data):
#     id = input('Введите id для удаления: ')
#     new_data = []
#     for elem in data:
#         if elem[0] != id:
#             new_data.append(elem)
#     return new_data


# def add_record(data):
#     id = input('Введите id нового человека: ')
#     name = input('Введите ФИО нового человека: ')
#     tel = input('Введите номер телефона: ')
#     data.append((id, name, tel))
#     return data

# def save(data):
#     with open('tel.txt', 'w', encoding='utf-8') as file:
#         for elem in data:
#             stroka = ';'.join(elem) + '\n'
#             file.write(stroka)


# def main():
#     my_choice = -1
#     changed = False
#     # словарь номеров команд и привязанных к ним функций
#     operations = {
#         1: printinfo,
#         2: export_to_csv,
#         3: search,
#         4: delete,
#         5: add_record
#         }
#     data = readfile('tel.txt')
#     while my_choice != 0:
#         menu()
#         my_choice = int(input('Введите команду: '))
#         if 1 <= my_choice <= 3:
#             operations[my_choice](data)
#         elif 4 <= my_choice <= 5:
#             changed = True
#             data = operations[my_choice](data)
#         elif my_choice == 0:
#             if changed:
#                 print('Данные были изменены. Идёт сохранение данных')
#                 save(data)
#             print('До свидания')
#         else:
#             print('Введена неправильная команда')


# if __name__ == '__main__':
#     main()
