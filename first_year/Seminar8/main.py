import os
from random import randint


# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.


def read_file():
    with open("c:/Users/Алексей/OneDrive/Desktop/Учеба/Знакомстов с языком python/Коды/PythonLessons/Seminar8/phonebook.txt", "r", encoding="utf - 8") as f:
        for string in f:
           temp = print(*string.strip().split(";"))
        return temp


def write_file():
    with open("c:/Users/Алексей/OneDrive/Desktop/Учеба/Знакомстов с языком python/Коды/PythonLessons/Seminar8/phonebook.txt", "a", encoding="utf - 8") as f:
        new_phone = input("Введите новую запись ").replace(" ", ";") + "\n"
        f.write(new_phone)


def menu():
    phone_list = read_file()
    while True:
        print("Нажмите 1 если хотите посмотреть справочник, Нажмите 2 если хотете внести запись или 3 что бы выйти из меню"
    )
        task_number = int(input("Укажите порядковый номер задачи, которую будем смотреть "))

        if task_number == 1:
            print(phone_list)
        elif task_number == 2:
            write_file()
        elif task_number == 0:
            break
        menu()


if __name__ == "__main__":
    menu()
