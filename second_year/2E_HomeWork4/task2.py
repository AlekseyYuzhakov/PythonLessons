import typing


def key_params(*args, **kwargs):
    temp_dict = {}
    print(args, kwargs)
    for k, i in kwargs.items():
        if k != "temp_dict":
            if isinstance(i, typing.Hashable):
                temp_dict.update({i: k})
            else:
                temp_dict.update({str(i): k})

    return temp_dict


params = key_params(
    name="Alice",
    age=30,
    scores=[85, 90, 78],
    info={"city": "New York", "email": "alice@example.com"},
)
print(params)


# a = 1
# b = 'hello'
# c = [1, 2, 3]
# d = {}

# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}


# a = 42
# b = 'hello'
# c = 3.14
# d = 'world'

# {42: 'a', 'hello': 'b', 3.14: 'c', 'world': 'd'}

# a = None
# b = ''
# c = []
# d = {}

# {None: 'a', '': 'b', '[]': 'c', '{}': 'd'}

# a = 42
# b = 'hello'
# c = 3.14
# d = 'world'

# {42: 'a', 'hello': 'b', 3.14: 'c', 'world': 'd'}

# a = True
# b = False
# c = True
# d = False

# {True: 'c', False: 'd'}

# name = 'Alice'
# age = 30
# scores = [85, 90, 78]
# info = {'city': 'New York', 'email': 'alice@example.com'}

# {'Alice': 'name', 30: 'age', '[85, 90, 78]': 'scores', "{'city': 'New York', 'email': 'alice@example.com'}": 'info'}
