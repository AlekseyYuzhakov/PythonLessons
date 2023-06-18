import os

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

os.system("cls")


def task2():
    print("Задача 2: Найдите сумму цифр трехзначного числа ")
    number = int(input("Введите число "))
    digitsum = 0
    n = number
    while n > 10:
        digitsum = digitsum + n % 10
        n = n // 10
    digitsum += n
    print("Сумма цифр в числе {} равна {}".format(number, digitsum))
    input("Нажмите любую клавишу что бы продолжить ")


task2()
os.system("cls")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def task4():
    print(
        "Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"
    )
    craneNumber = int(input("Введите число журавликов "))
    check6 = bool(craneNumber % 6 == 0)
    Katecrane = 0
    if check6:
        Katecrane = craneNumber // 3 * 2
        Pitsergcrane = craneNumber - Katecrane
        print(
            "Катя собрала {} журавликов(а), а Петя и Сережа по {} ".format(
                Katecrane, Pitsergcrane // 2
            )
        )
    else:
        print("Нет удовлетворяющего решения ")
    input("Нажмите любую клавишу что бы продолжить ")


task4()
os.system("cls")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no


def task6():
    print(
        "Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета."
    )
    ticketNumber = int(input("Введите номер вашего билета "))
    TicketCheck = bool(len(str(ticketNumber)) == 6)
    # print("TicketCheck", TicketCheck)
    firstdigits = int(ticketNumber // 1000)
    # print("firstdigits", firstdigits)
    sumofFirstDigits = 0
    sumofSecondDigits = 0
    if TicketCheck:
        while ticketNumber > 999:
            sumofFirstDigits = sumofFirstDigits + firstdigits % 10
            firstdigits = firstdigits // 10
            # print("sumofFirstDigits ", sumofFirstDigits)
            sumofSecondDigits = sumofSecondDigits + ticketNumber % 10
            # print("sumofSecondDigits ", sumofSecondDigits)
            ticketNumber = ticketNumber // 10
            # print("ticketNumber ", ticketNumber)
        equalCheck = bool(sumofFirstDigits == sumofSecondDigits)
        print("Билет счастливый )) ", equalCheck)
    else:
        print("Не в билетах счятье ))")
    input("Нажмите любую клавишу что бы продолжить ")


task6()
os.system("cls")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


def task8():
    print(
        "Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)."
    )
    ChocoLenght = int(input("Укажитет длиину плитки "))
    ChocoWidth = int(input("Укажитет ширину плитки "))
    ChocoNumber = int(input("Укажитет сколько долех хотите взять "))
    if (ChocoLenght % ChocoNumber == 0) or (ChocoWidth % ChocoNumber == 0):
        print("Можно отломить ))")
    elif ChocoNumber % ChocoLenght == 0 or ChocoNumber % ChocoWidth == 0:
        print("Можно отломить ))")
    else:
        print("Сегодня без шоколадки ((")

    input("Нажмите любую клавишу что бы продолжить ")


task8()

print("Спасибо ")
