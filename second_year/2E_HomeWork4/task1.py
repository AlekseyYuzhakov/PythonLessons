# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки



def transpose(matrix):
    temp_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp_matrix[j][i] = matrix[i][j]

    return temp_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
transposed_matrix = transpose(matrix)

print(matrix)
print(transposed_matrix)

# Введите ваше решение ниже
