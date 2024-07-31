import unittest


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
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def birthday(self):

        self._age += 1

    def get_age(self):
        return self._age


class test_employee(Person):
    MAX_LEVEL = 7

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
            raise InvalidIdError(id)
        self.id = id
        self.ocupation = ocupation
        self.salary = salary

    def get_level(self):
        sum_digits = 0
        for digit in str(self.id):
            sum_digits += int(digit)
        return sum_digits % 7

    def raise_salary(self, value):

        self.salary *= 1 + value / 100

    def __str__(self) -> str:

        return (
            f"{self.last_name} {self.first_name} {self.patronymic} ({self.ocupation})"
        )


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.emp = test_employee(
            "Ivanov", "Ivan", "Ivanovich", 30, 123456, "Manager", 50000
        )

    def test_employee_full_name(self):
        self.assertEqual(self.emp.full_name(), "Ivanov Ivan Ivanovich")
    
    def test_employee_birthday(self):
        self.emp.birthday()
        self.assertEqual(self.emp._age, 31)
    
    def test_employee_raise_salary(self):
        self.emp.raise_salary(10)
        self.assertEqual(self.emp.salary, 55000.0)
      
    def test_employee_str(self):
        self.assertEqual("Ivanov Ivan Ivanovich (Manager)", self.emp.__str__())
      
    def test_employee_last_name_title(self):
        self.assertTrue(self.emp.last_name.istitle())


if __name__ == "__main__":
    
    assert_answer = "Ivanov Ivan Ivanovich"
    emp = test_employee(
            "Ivanov", "Ivan", "Ivanovich", 30, 123456, "Manager", 50000
        )
    print(assert_answer == emp.full_name())



    unittest.main()
