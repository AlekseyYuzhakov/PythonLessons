import logging


class Rectangle:
    """
    >>> r1 = Rectangle(5)
    >>> r1.width == 5
    True
    >>> r2 = Rectangle(-2)
    Traceback (most recent call last):
      ...
    NegativeValueError: Ширина должна быть положительной, а не -2
    >>> r2 = Rectangle(3,4)
    >>> r2.width == 3
    True
    >>> r2.height == 4
    True
    >>> r1.perimeter()
    20
    >>> r2.perimeter()
    14
    >>> r1.area()
    25
    >>> r2.area()
    12
    >>> r3 = r1 + r2
    >>> r3.width
    8
    >>> r3.height
    9.0
    >>> r3 = r1 - r2
    >>> r3.width
    2
    >>> r3.height
    1.0

    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

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

    def __init__(self, width, height=None):
        if width <= 0:
            e = f"Ширина должна быть положительной, а не {width}"
            self.loger.error(msg=e)
            raise NegativeValueError(e)
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                e = f"Высота должна быть положительной, а не {height}"
                self.loger.error(msg=e)
                raise NegativeValueError(e)
            self._height = height

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self._width + self._height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self._width * self._height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self._width} и {self._height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self._width}, {self._height})"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            e = f"Ширина должна быть положительной, а не {value}"
            self.loger.error(msg=e)
            raise NegativeValueError(e)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            e = f"Высота должна быть положительной, а не {value}"
            self.loger.error(msg=e)
            raise NegativeValueError(e)
        self._height = value


class NegativeValueError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
