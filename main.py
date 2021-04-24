## Sudoku Solver ##
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solve(board):
    if board is None:
        return []
    if find_zero(board) is None:
        return board
    else:
        zero = find_zero(board)
        pos_row, pos_col = zero[0], zero[1]
    for i in range(1, 10):
        if is_valid(board, pos_row, pos_col, i):
            board[pos_row][pos_col] = i
            # print_board(board)
            # print("\n")
            if solve(board):
                return board
            board[pos_row][pos_col] = 0
    return False


def print_board(board):
    for row in board:
        string_to_print = ""
        for value in row:
            string_to_print += str(value) + " "
        print(string_to_print)


def create_parts(board):
    parts = []
    num_row = len(board)
    num_col = len(board[0])
    diff1 = 0
    diff2 = 0
    part = []
    for p in range(0, 9):
        if p > 0:
            parts.append(part)
            part = []
            diff1 += 3
            if p == 3 or p == 6:
                diff2 += 3
                diff1 = 0
        for i in range(0, num_row):
            for j in range(0, num_col):
                if diff2 <= i < (3 + diff2) and diff1 <= j < (3 + diff1):
                    part.append(board[i][j])
    parts.append(part)
    return parts


def find_zero(board):
    if board == []:
        return []
    num_row = len(board)
    num_col = len(board[0])
    zero_pos = []
    for i in range(0, num_row):
        for j in range(0, num_col):
            if board[i][j] == 0:
                zero_pos.append(i)
                zero_pos.append(j)
                return zero_pos
    return None


def is_valid(board, pos_row, pos_col, value):
    parts = create_parts(board)
    num_row = len(board)
    num_col = len(board[0])

    if board is None:
        print("Board is empty")
        return False
    elif not (1 <= int(value) <= 9):
        print("Wrong value")
        return False
    elif not (0 <= pos_row <= (num_row - 1) or 0 <= (pos_col <= num_col - 1)):
        print("Out of bound")
        return False
    elif board[pos_row][pos_col] == 0:
        if value in board[pos_row]:
            return False
        for i in range(0, num_col):
            if value == board[i][pos_col]:
                return False
        if 0 <= pos_row < 3 and 0 <= pos_col < 3:
            if value in parts[0]:
                return False
            else:
                return True
        if 0 <= pos_row < 3 and 3 <= pos_col < 6:
            if value in parts[1]:
                return False
            else:
                return True
        if 0 <= pos_row < 3 and 6 <= pos_col < 9:
            if value in parts[2]:
                return False
            else:
                return True
        if 3 <= pos_row < 6 and 0 <= pos_col < 3:
            if value in parts[3]:
                return False
            else:
                return True
        if 3 <= pos_row < 6 and 3 <= pos_col < 6:
            if value in parts[4]:
                return False
            else:
                return True
        if 3 <= pos_row < 6 and 6 <= pos_col < 9:
            if value in parts[5]:
                return False
            else:
                return True
        if 6 <= pos_row < 9 and 0 <= pos_col < 3:
            if value in parts[6]:
                return False
            else:
                return True
        if 6 <= pos_row < 9 and 3 <= pos_col < 6:
            if value in parts[7]:
                return False
            else:
                return True
        if 6 <= pos_row < 9 and 6 <= pos_col < 9:
            if value in parts[8]:
                return False
            else:
                return True

