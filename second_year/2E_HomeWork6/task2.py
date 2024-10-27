queens = [(3, 4), (5, 5), (8, 1), (1, 3), (2, 8), (4, 7), (7, 6), (6, 2)]


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q2[0] - q1[0]) == abs(q2[1] - q1[1]):
        return False
    return True


def check_queens(queens):
    if len(queens)<8:
        return True
    answer = []
    for q1 in range(len(queens)):
        for q2 in range(q1, len(queens)):
            answer.append(is_attacking(queens[q1], queens[q2]))

    return all(answer)


print(check_queens(queens))
