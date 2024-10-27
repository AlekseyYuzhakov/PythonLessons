def print_info(temp):
    print(temp)


def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()
    return temp

def write_file():
    pass

def menu():
    data = read_file()
    while True:
        print('Выберите действие: ')
        print('1 - вывести инфо на экран')
        print('0 - выход из программы')
        n = int(input('ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        # elif n == 3:
        #     data = append(data)


if __name__ == '__main__':
    menu()
