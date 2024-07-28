import string

a = "Иван Иванов"
for char in a:
    if char in string.digits:
        print("Да")
