У вас есть два класса: Person и Employee из предыдущих задач.

Необходимо написать тесты с использованием модуля pytest и лежать в class TestEmployee.

*Тесты необходимо написать именно в этом порядке!

Тесты:

test_employee_full_name: Тестирование метода full_name(). Создайте объект Employee с фамилией "Ivanov", именем "Ivan", отчеством "Ivanovich" и убедитесь, что метод full_name() возвращает правильное полное имя в формате "Ivanov Ivan Ivanovich".

test_employee_birthday: Тестирование метода birthday(). Создайте объект Employee с возрастом 30, вызовите метод birthday() и убедитесь, что возраст увеличился на 1 и стал равным 31.

test_employee_raise_salary: Тестирование метода raise_salary(). Создайте объект Employee с зарплатой 50000, вызовите метод raise_salary(10) и убедитесь, что зарплата увеличилась на 10% и стала равной 55000.0.

test_employee_str: Тестирование метода __str__(). Создайте объект Employee с данными: фамилия "Ivanov", имя "Ivan", отчество "Ivanovich", возраст 30, должность "manager" и зарплата 50000. Убедитесь, что метод __str__() возвращает правильную строку в формате "Ivanov Ivan Ivanovich (Manager)".

test_employee_last_name_title: Тестирование атрибута last_name. Создайте объект Employee с фамилией "Ivanov" и убедитесь, что атрибут last_nameвозвращается в верхнем регистре, то есть "Ivanov".