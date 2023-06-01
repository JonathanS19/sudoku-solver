import numpy as np

board = np.array(
    [
        [0, 0, 2, 0, 0, 0, 4, 0, 0],
        [6, 0, 1, 0, 0, 0, 2, 0, 7],
        [0, 0, 0, 7, 5, 2, 0, 0, 0],
        [0, 0, 6, 2, 7, 1, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 5, 3, 8, 1, 0, 0],
        [0, 0, 0, 6, 1, 9, 0, 0, 0],
        [1, 0, 9, 0, 0, 0, 8, 0, 6],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
    ],
    dtype="int8",
)
rest = []
stack = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            rest.append((i, j))


def solve(pos):
    numbers = find_possible_nums(board, pos)
    for num in numbers:
        board[pos] = num
        if rest == []:
            return
        new_pos = Push()
        solve(new_pos)
        if rest == []:
            return
        Pop()
        board[pos] = 0


def check_validity(board: np.array, position: tuple, num: int) -> bool:
    row, col = position
    if num in board[row]:
        return False
    if num in board[:, col]:
        return False
    if num in board[row // 3 * 3 : row // 3 * 3 + 3, col // 3 * 3 : col // 3 * 3 + 3]:
        return False
    return True


def find_possible_nums(board: np.array, position: tuple) -> list:
    row, col = position
    possible = []
    for num in range(1, 10):
        if check_validity(board, position, num):
            possible.append(num)
    return possible


def Push() -> tuple:
    pos = rest.pop()
    stack.append(pos)
    return pos


def Pop() -> tuple:
    pos = stack.pop()
    rest.append(pos)
    return pos

print(board)
