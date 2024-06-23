lst = [1, 1, 1, 1, 1, 1]  # [1, 1, 2, 2, 3, 3]

new_lst = []
for i in lst:
    if lst.count(i) > 1:
        if i not in new_lst:
            new_lst.append(i)

print(new_lst)


# lst = [1, 2, 3, 4, 5]
# Ожидаемый ответ:
# []

# lst = [1, 2, 3, 2, 4, 5, 4]
# Ожидаемый ответ:
# [2, 4]

# lst = [1, 2, 3, 4, 5, 6, 7]
# Ожидаемый ответ:
# []
