import random as rnd
import logging
from Employee import Employee
from Rectangle import Rectangle


class Station:
    """
    Класс, представляющий робочее место.

    Атрибуты:
    - __PARTITION_SIZE : обьем производимой партии

    Методы:
    - Produce_partition(): метод создающий партию

    """

    loger = logging.getLogger(__name__)
    my_format = "{levelname:<2} - {asctime:<2} - {msg} -"
    logging.basicConfig(
        filename="D://GBru//Учеба//Enter_python//Code//PythonLessons//2E_HomeWork15//station.log",
        filemode="a",
        encoding="UTF-8",
        level="INFO",
        style="{",
        format=my_format,
    )

    __PARTITION_SIZE = 20

    def __init__(self, worker: Employee) -> None:
        """
        Инициализация рабочего места, с привязкой персонала

        """
        self.worker = worker
        self.partition = []
        self.fail_count = 0

    def produce_partition(self, width: int, height: int):
        """
        Производим партию продукта
        """
        while len(self.partition) < self.__PARTITION_SIZE:
            """
            width_option и height_option необходимы для имитации 5% брака при производстве
            """
            width_option = [width for i in range(self.__PARTITION_SIZE)]
            width_option.append(width + 1)
            width_option.append(width + 2)
            height_option = [height for i in range(self.__PARTITION_SIZE)]
            height_option.append(height + 1)
            height_option.append(height + 2)

            steel_sheet = Rectangle(rnd.choice(width_option), rnd.choice(height_option))
            self.partition.append(steel_sheet)

            if steel_sheet.width != width or steel_sheet.height != height:
                self.fail_count += 1

        self.worker.change_salary(-self.fail_count * 5)
        self.loger.info(
            msg=f"worker:{self.worker}, produce:{self.__PARTITION_SIZE-self.fail_count} steel_sheetы with {self.fail_count} failed. Ernd salary is {self.worker.salary}"
        )


class Work_site:
    """
    Класс, представляющий цех.

    Атрибуты:
    - list_of_workers : перчень рабочих

    Методы:
    - hire_worckers(): создает рабочих
    - fill_stations(): распределяет рабочих по станциям
    - start_shift (): запускает смену
    """

    def __init__(self) -> None:
        pass

    loger = logging.getLogger(__name__)
    my_format = "{levelname:<2} - {asctime:<2} - {msg} -"
    logging.basicConfig(
        filename="work_site.log",
        filemode="a",
        encoding="UTF-8",
        level="INFO",
        style="{",
        format=my_format,
    )

    list_of_workers = []

    def hire_worckers(self):
        List_of_first_names = ["Ivan", "Alex", "Victor"]
        List_of_last_names = ["Ivanov", "Volkov", "Serov"]
        List_of_patronymic_names = ["Ivanovich", "Petrovich", "Kuzmich"]

        list_of_worckers = []
        for i in range(len(List_of_last_names)):
            new_worcker = Employee(
                rnd.choice(List_of_last_names),
                rnd.choice(List_of_first_names),
                rnd.choice(List_of_patronymic_names),
                rnd.randint(18, 65),
                rnd.randint(100_000, 999_999),
                "fabricator",
                5000,
            )
            self.loger.info(
                msg=f"hired worker:{new_worcker}, age:{new_worcker._age} with salary {new_worcker.salary}"
            )
            list_of_worckers.append(new_worcker)
        return list_of_worckers

    def fill_stations(self, list_of_worckers):
        list_of_stations = {}
        for i in range(len(list_of_worckers)):
            worker = list_of_worckers.pop()
            new_station = Station(worker)
            list_of_stations.setdefault(i, new_station)
            self.loger.info(msg=f"worker:{worker}, assigned to station number {i+1}")
        return list_of_stations

    def start_shift(self):
        self.loger.info(msg=f"shift started")
        list_of_worckers = self.hire_worckers()
        list_of_stations = self.fill_stations(list_of_worckers)
        for i in range(len(list_of_stations)):
            list_of_stations[i].produce_partition(
                rnd.randint(2, 10), rnd.randint(2, 10)
            )
        self.loger.info(msg=f"shift is over")
        print("shift is over")
