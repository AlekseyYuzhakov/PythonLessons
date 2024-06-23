text = (
    "Hello world. Hello Python. Hello again.".lower()
    .replace(".", " ")
    .replace(",", " ")
    .replace("!", " ")
    .replace("'", " ")
    .split()
)

new_dict = {}
for elem in text:
    if elem.isdigit():
        pass
    elif elem in new_dict:
        new_dict[elem] += 1
    else:
        new_dict[elem] = 1
list_of_words = []
for k, v in new_dict.items():
    list_of_words.append((k, v))
list_of_words = sorted(list_of_words, key=lambda v: v[0], reverse=True)
list_of_words = sorted(list_of_words, key=lambda v: v[1], reverse=True)

print(list_of_words[:10:])


# text = "Hello world. Hello Python. Hello again."

# text = 'This is a sample text without repeating words.'
# Ожидаемый ответ:
# [('words', 1), ('without', 1), ('this', 1), ('text', 1), ('sample', 1), ('repeating', 1), ('is', 1), ('a', 1)]

# text = "Python 3.9 is the latest version of Python. It's awesome!"
# Ожидаемый ответ:
# [('python', 2), ('version', 1), ('the', 1), ('s', 1), ('of', 1), ('latest', 1), ('it', 1), ('is', 1), ('awesome', 1)]


# text = 'Python is python, is, IS, and PYTHON.'
# Ожидаемый ответ:
# [('python', 3), ('is', 3), ('and', 1)]

# text = "The quick brown fox jumps over the lazy dog. Lazy dog, lazy fox!"
# Ожидаемый ответ:
# [('lazy', 3), ('the', 2), ('fox', 2), ('dog', 2), ('quick', 1), ('over', 1), ('jumps', 1), ('brown', 1)]
