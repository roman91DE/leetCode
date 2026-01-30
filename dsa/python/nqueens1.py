type board = list[int]


def empty_board(n: int) -> board:
    return [-1 for _ in range(n)]


def place_queen(b: board, row: int, col: int) -> board:
    new_board = b.copy()
    new_board[row] = col
    return new_board


def can_place_queen(b: board, row: int, col: int) -> bool:
    if b[row] != -1:
        return False  # There's already a queen in this row
    if col in b:
        return False  # There's already a queen in this column
    for r, c in enumerate(b):
        if r == row:
            continue
        if row - r == abs(col - c):
            return False  # There's already a queen in this diagonal
    return True


def backtrack(b: board, row: int = 0):
    if row == len(b):
        yield b
        return
    for col in range(len(b)):
        if can_place_queen(b, row, col):
            new_board = place_queen(b, row, col)
            yield from backtrack(new_board, row + 1)


def strconv(b: board) -> list[str]:
    acc = []
    for row in b:
        line = ["."] * len(b)
        line[row] = "Q"
        acc.append("".join(line))
    return acc


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        g = backtrack(empty_board(n))
        return [strconv(b) for b in g]
