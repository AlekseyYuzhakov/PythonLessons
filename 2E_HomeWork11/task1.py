"""
Разработайте программное обеспечение для ведения журнала событий. Вам необходимо создать класс, который будет представлять строки журнала и включать в себя информацию об авторе и времени создания каждой записи.

Условие задачи:

Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты и методы:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'.

Магические методы (Dunder-методы):

Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author. Метод также автоматически фиксирует время создания записи. В этом методе создается новый объект MyStr с указанными атрибутами и текущим временем в атрибуте time.

Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.  
Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объектаMyStrс теми же значениямиvalueиauthor`.

Пример использования.
На входе:


event = MyStr("Завершилось тестирование", "John")
print(event)
На выходе:


Завершилось тестирование (Автор: John, Время создания: [ в формате '%Y-%m-%d %H:%M'])
На входе:


my_string = MyStr("Пример текста", "Иван")
print(my_string)
На выходе:


Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)
На входе:


my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))
На выходе:


MyStr('Мама мыла раму', 'Маршак')
"""

from datetime import datetime


class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        return instance

    def __init__(self, value, author) -> None:
        self.author = author
        self.value = value
        self.time = datetime.now()

    def __str__(self) -> str:
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time.strftime('%m/%d/%Y, %H:%M')})"

    def __repr__(self) -> str:
        return f"MyStr{self.value, self.author}"


a = MyStr("Эх вася вася", "Вася")
print(a)
print(repr(a))
