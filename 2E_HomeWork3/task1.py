items = {"ключи": 0.3, "кошелек": 0.2, "телефон": 0.5, "зажигалка": 0.1}
max_weight = 1.0

backpack = {}
backpack_weight = 0
for k, v in items.items():
    if k not in backpack.keys():
        if max_weight > backpack_weight:
            backpack_weight += v
            backpack.setdefault(k, v)
