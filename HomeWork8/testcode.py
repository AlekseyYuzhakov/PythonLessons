list_list = [
    "Петров Василий Иванович",
    "Антонов Иван Сергеевич",
    "Герасимов Дмитрий Семенович",
    "Дмитриев Виктор Васильевич",
    "Южаков Алексей Сергеевич",
]
serch = "Южаков"
pos = 0
for elem in list_list:
    if serch in elem:
        list_list.pop(pos)
    pos += 1

print(*list_list, sep="\n")
