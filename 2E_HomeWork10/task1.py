"""
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.

Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".

Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".

Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:

animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного типа животного. Количество и типы аргументов могут различаться в зависимости от типа животного.

Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.

Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением 'Недопустимый тип животного'.
"""


class Animal:
    name = ""

    def __init__(self, name) -> None:
        self.name = name


class Bird(Animal):
    wingspan = 0

    def __init__(self, name, wingspan) -> None:
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan


class Fish(Animal):
    max_depth = 0

    def __init__(self, name, max_depth) -> None:
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    weight = 0

    def __init__(self, name, weight) -> None:
        super().__init__(name)
        self.weight = weight

    def category(self):

        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory(Bird, Fish, Mammal):
     
    def create_animal(kind, name, *args):
        animal = None
        match kind:
            case "Bird":
                animal = Bird(name, args[0])
                return animal
            case "Fish":
                animal = Fish(name, args[0])
                return animal
            case "Mammal":
                animal = Mammal(name, args[0])
                return animal
            case _:
                raise ValueError("Недопустимый тип животного")


animal1 = AnimalFactory.create_animal("Bird", "Орел", 200)
animal2 = AnimalFactory.create_animal("Fish", "Лосось", 50)
animal3 = AnimalFactory.create_animal("Mammal", "Слон", 5000)


print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())
