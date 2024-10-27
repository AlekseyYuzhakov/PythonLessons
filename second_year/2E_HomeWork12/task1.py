"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 
Если ФИО не соответствует условию, выведите:
ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). В противном случае выведите:
Оценка должна быть целым числом от 2 до 5
Результат теста должен быть целым числом от 0 до 100

○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана следующая информация.
Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по предметам. Класс должен иметь следующие методы:

Атрибуты класса:
name (str): ФИО студента. 
subjects (dict): Словарь, который хранит предметы в качестве ключей и информацию об оценках и результатах тестов для каждого предмета в виде словаря.


Магические методы (Dunder-методы):
__init__(self, name, subjects_file): Конструктор класса. 
Принимает имя студента и файл с предметами и их результатами. 
Инициализирует атрибуты name и subjects и вызывает метод load_subjects для загрузки предметов из файла.

__setattr__(self, name, value): Дескриптор, который проверяет установку атрибута name. 
Убеждается, что name начинается с заглавной буквы и состоит только из букв.

__getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок и результатов тестов) по их именам.

__str__(self): Возвращает строковое представление студента, включая имя и список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:
load_subjects(self, subjects_file): 
Загружает предметы из файла CSV. Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут subjects.

add_grade(self, subject, grade): Добавляет оценку по заданному предмету. Убеждается, что оценка является целым числом от 2 до 5.

add_test_score(self, subject, test_score): Добавляет результат теста по заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.

get_average_test_score(self, subject): Возвращает средний балл по тестам для заданного предмета.

get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:

student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

На выходе:

Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""

import string


class CheckData:

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value: str):
        if not value.istitle():
            raise ValueError(
                "ФИО должно состоять только из букв и начинаться с заглавной буквы"
            )
        for char in value:
            if char in string.digits:
                raise ValueError(
                    "ФИО должно состоять только из букв и начинаться с заглавной буквы"
                )
        return value


class Student:
    name = CheckData()
    subjects: dict = {}

    def __init__(self, name="", subjects={}) -> None:
        self.name = name
        self.subjects = self.load_subjects(subjects)

    def add_grade(self, subject, score):
        if not subject in self.subjects.keys():
            raise ValueError(f"Предмет {subject} не найден")
        elif str.isdigit(str(score)) and 2 <= score <= 5:
            score = ("grade", score)
            for k, v in self.subjects.items():
                if k == subject:
                    self.subjects[k].append(score)
        else:
            raise ValueError("Оценка должна быть целым числом от 2 до 5 ")

    def add_test_score(self, subject, score):
        if not subject in self.subjects.keys():
            raise ValueError(f"Предмет {subject} не найден")
        elif str.isdigit(str(score)) and 0 <= score <= 100:
            score = ("test", score)
            for k, v in self.subjects.items():
                if k == subject:
                    self.subjects[k].append(score)
        else:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100 ")

    def get_average_grade(self, subject=None):
        avg_grd = 0
        count = 0
        if subject is None:
            for list in self.subjects.values():
                for item in list:
                    if item[0] == "grade":
                        avg_grd += item[1]
                        count += 1
        elif subject in self.subjects.keys():
            for item in self.subjects[subject]:
                if item[0] == "grade":
                    avg_grd += item[1]
                    count += 1
        else:
            raise ValueError(f"Предмет {subject} не найден")
        if count > 0 and avg_grd > 0:
            return avg_grd / count
        return None

    def get_average_test_score(self, subject=None):
        avg_grd = 0
        count = 0
        if subject is None:
            for list in self.subjects.values():
                for item in list:
                    if item[0] == "test":
                        avg_grd += item[1]
                        count += 1
        elif subject in self.subjects.keys():
            for item in self.subjects[subject]:
                if item[0] == "test":
                    avg_grd += item[1]
                    count += 1
        else:
            raise ValueError(f"Предмет {subject} не найден")
        if count > 0 and avg_grd > 0:
            return avg_grd / count
        return None

    def load_subjects(self, file_path):
        temp_dict = {}
        with open(file_path, "r") as file:
            for line in file:
                for word in line.split(","):
                    temp_dict.setdefault(word, [])
        return temp_dict

    def __str__(self) -> str:
        subject = []
        for k, v in self.subjects.items():
            if len(v) > 0:
                subject.append(k)
        return f"Студент: {self.name} \nПредметы: {', '.join(subject)}"


student = Student("Иван Иванов", "2E_HomeWork12/subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)
