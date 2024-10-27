import random as rnd


board_list = []


def is_attacking(q1, q2):
    if (q1[0] == q2[0] or q1[1] == q2[1] or abs(q2[0] - q1[0]) == abs(q2[1] - q1[1])):
        return False
    return True


def check_queens(queens):
    for q1 in range(len(queens) - 1):
        for q2 in range(q1 + 1, len(queens)):
            if is_attacking(queens[q1], queens[q2]) == False:
                return False
    return True


def generate_boards():
    global board_list
    combinations_count = 0
    while combinations_count < 4:
        x = [1, 2, 3, 4, 5, 6, 7, 8]
        y = [1, 2, 3, 4, 5, 6, 7, 8]
        queens = []
        queens.append((rnd.choice(x), rnd.choice(y)))
        x.remove(queens[0][0])
        y.remove(queens[0][1])
        for _ in range(1, 8):
            q = (rnd.choice(x), rnd.choice(y))
            x.remove(q[0])
            y.remove(q[1])
            queens.append(q)
        if check_queens(queens):
            board_list.append(queens)
            combinations_count += 1

    return board_list


board_list = generate_boards()

for board in board_list:
    print(board)
