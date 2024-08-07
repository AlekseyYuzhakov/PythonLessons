import logging


class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid name: {self.name}. Name should be a non-empty string."


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Invalid age: {self.age}. Age should be a positive integer."


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999."


class Person:
    loger = logging.getLogger(__name__)
    my_format = "{levelname:<2} - {asctime:<2} - {msg} -"
    logging.basicConfig(
        filename="D://GBru//Учеба//Enter_python//Code//PythonLessons//2E_HomeWork15//LOG.log",
        filemode="a",
        encoding="UTF-8",
        level="INFO",
        style="{",
        format=my_format,
    )

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            e = InvalidNameError(last_name).__str__()
            self.loger.error(msg=e)
            raise InvalidNameError(e)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            e = InvalidNameError(first_name).__str__()
            self.loger.error(msg=e)
            raise InvalidNameError(e)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            e = InvalidNameError(patronymic).__str__()
            self.loger.error(msg=e)
            raise InvalidNameError(e)
        if not isinstance(age, int) or age <= 0:
            e = InvalidAgeError(age).__str__()
            self.loger.error(msg=e)
            raise InvalidAgeError(e)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 123456, 'manager', 50000)
        >>> emp1.full_name()
        'Ivanov Ivan Ivanovich'

        """
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 123456, 'manager', 50000)
        >>> emp1.birthday()
        >>> emp1.get_age()
        31

        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    """
        >>> emp1 = Employee("ivanov", "ivan", "ivanovich", 30, 123456, 'manager', 50000)
        >>> emp1.last_name
        'Ivanov'
        """

    def __init__(
        self,
        last_name: str,
        first_name: str,
        patronymic: str,
        age: int,
        id: int,
        ocupation: str,
        salary: int,
    ):
        super().__init__(last_name, first_name, patronymic, age)
        if not isinstance(id, int) or id < 100_000 or id > 999_999:
            e = InvalidIdError(id).__str__()
            self.loger.error(msg=e)
            raise InvalidIdError(id)
        self.id = id
        self.ocupation = ocupation
        self.salary = salary

    def get_level(self):
        sum_digits = 0
        for digit in str(self.id):
            sum_digits += int(digit)
        return sum_digits % 7

    def change_salary(self, value):
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 123456, 'manager', 50000)
        >>> emp1.raise_salary(10)
        >>> emp1.salary
        55000.0
        """
        self.salary = round(self.salary * (1 + value / 100), 2)

    def __str__(self) -> str:
        """
        >>> emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, 123456, 'Manager', 50000)
        >>> emp1.__str__()
        'Ivanov Ivan Ivanovich (Manager)'
        """
        return (
            f"{self.last_name} {self.first_name} {self.patronymic} ({self.ocupation})"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
