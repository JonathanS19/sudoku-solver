import numpy as np
import tkinter

board = np.zeros((9, 9), dtype="int8")

board_window = tkinter.Tk()
board_window.wm_title("TEST")
board_numbers = tkinter.Frame(board_window)
board_selection = tkinter.Frame(board_window)
board_numbers.pack()
board_selection.pack()

number = tkinter.IntVar()
selections = [
    tkinter.Radiobutton(board_selection, text=str(i + 1), variable=number, value=i + 1)
    for i in range(9)
]
for i in range(9):
    selections[i].grid(row=1, column=i)
tkinter.Button(board_selection, text="Clear", command=lambda: clear_board()).grid(
    row=2, column=0, columnspan=9
)
tkinter.Button(board_selection, text="Solve", command=lambda: solve_d()).grid(
    row=3, column=0, columnspan=9
)

grid = [
    [tkinter.Button(board_numbers, text=str(board[i][j])) for j in range(9)]
    for i in range(9)
]
for i in range(9):
    for j in range(9):
        grid[i][j].config(command=lambda i=i, j=j: set_number(grid[i][j], (i, j)))
        grid[i][j].grid(row=(i+(i//3)), column=(j+(j//3)))
for i in range(3,9,4):
    for j in range(9):
        tkinter.Label(board_numbers, text="-").grid(row=i, column=j+j//3)
        tkinter.Label(board_numbers, text="|").grid(row=j+j//3, column=i)
tkinter.Label(board_numbers, text="+").grid(row=3, column=3)
tkinter.Label(board_numbers, text="+").grid(row=3, column=7)
tkinter.Label(board_numbers, text="+").grid(row=7, column=3)
tkinter.Label(board_numbers, text="+").grid(row=7, column=7)

def clear_board():
    global board
    number.set(0)
    board = np.zeros((9, 9), dtype="int8")
    for i in range(9):
        for j in range(9):
            grid[i][j].config(text="0")
        print()


def set_number(button, position):
    num = number.get()
    if check_validity(position, num):
        board[position] = num
        button.config(text=str(num))


def check_validity(board: np.array, position: tuple, num: int) -> bool:
    row, col = position
    if num in board[row]:
        return False
    if num in board[:, col]:
        return False
    if num in board[row // 3 * 3 : row // 3 * 3 + 3, col // 3 * 3 : col // 3 * 3 + 3]:
        return False
    return True


def solve_d():
    global board
    board = solver(board)
    for i in range(9):
        for j in range(9):
            grid[i][j].config(text=str(board[i][j]))


def solver(board: np.array):
    rest = []
    stack = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                rest.append((i, j))

    def Push() -> tuple:
        pos = rest.pop()
        stack.append(pos)
        return pos
    
    def Pop() -> tuple:
        pos = stack.pop()
        rest.append(pos)
        return pos
    
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

    solve(Push())

def find_possible_nums(board: np.array, position: tuple) -> list:
    row, col = position
    possible = []
    for num in range(1, 10):
        if check_validity(board, position, num):
            possible.append(num)
    return possible


if __name__ == "__main__":
    board_window.mainloop()
