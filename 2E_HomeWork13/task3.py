"""
В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.

Ваша задача:
Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных."""


class Person:

    def __init__(self, surname: str, name: str, fathername: str, age: int) -> None:
        if not surname.isalpha():
            raise InvalidNameError(
                f"Invalid name: . Name should be a non-empty string."
            )
        self._surname = surname
        if not name.isalpha():
            raise InvalidNameError(
                f"InvalidNameError: Name must be non empty string. you enter [{name}]"
            )
        self._name = name
        if not fathername.isalpha():
            raise InvalidNameError(
                f"InvalidNameError: Fathername must be non empty string. you enter [{fathername}]"
            )
        self._fathername = fathername
        if age <= 0:
            raise InvalidAgeError(
                f"Invalid age: {age}. Age should be a positive integer."
            )
        self._age = age

    def __str__(self) -> str:
        return f"surname:{self._surname}, name:{self._name}, fathername:{self._fathername}, age:{self._age}"

    def get_age(self):
        return self._age

    def birthday(self):
        self._age += 1


class Employee(Person):

    def __init__(
        self, surname: str, name: str, fathername: str, age: int, ID: int
    ) -> None:
        super().__init__(surname, name, fathername, age)
        if not 100000 < ID < 999999:
            raise InvalidIdError(
                f"Invalid id: {ID}. Id should be a 6-digit positive integer between 100000 and 999999"
            )
        self._ID = ID

    def get_level(self):
        sum_digits = 0
        for digit in str(self._ID):
            sum_digits += int(digit)
        return sum_digits

    def __str__(self) -> str:
        return f"surname:{self._surname}, name:{self._name}, fathername:{self._fathername}, age:{self._age}, Level:{self.get_level()%7}"


class InvalidNameError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidAgeError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class InvalidIdError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
print(employee)


"""
class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError(patronymic)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id: int):
        super().__init__(last_name, first_name, patronymic, age)
        if not isinstance(id, int) or id < 100_000 or id > 999_999:
            raise InvalidIdError(id)

        self.id = id

    def get_level(self):
        s = sum(num for num in str(self.id))
        return s % self.MAX_LEVEL"""