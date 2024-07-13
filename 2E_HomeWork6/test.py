import random as rnd


def generate_board(size):
    board = []
    for i in range(size):
        rand_row = rnd.randint(1, size)
        board.append((i + 1, rand_row))
    return board


def check_board(board):
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if (board[i][0] == board[j][0] or board[i][1] == board[j][1] or abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1])):
                return False
    return True


def find_succesfull_board(size, count):
    succesfull_board = []
    while len(succesfull_board) < count:
        board = generate_board(size)
        if check_board(board):
            succesfull_board.append(board)
    return succesfull_board


board_list = find_succesfull_board(8, 4)

for board in board_list:
    print(board)
