"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
Пример выходных данных:


Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]


class LotteryGame:
    my_list = []
    numbers = []

    def __init__(self, my_list: list, numbers: list) -> None:
        self.my_list = my_list
        self.numbers = numbers

    def compare_lists(self):
        res = []
        for obj in self.my_list:
            if obj in self.numbers:
                res.append(obj)
        if len(res):
            print(f"Совпадающие числа: {res}")
            print(f"Количество совпадающих чисел: {len(res)}")
        else:
            print(f"Совпадающих чисел нет.")


game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
