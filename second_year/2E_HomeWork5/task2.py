names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]


print(
    {
        names[i]: round((salary[i] * (int(bonus[i].replace("%", ""))) / 100), 1)
        for i in range(len(names))
    }
)

