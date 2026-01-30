from typing import List
from itertools import chain
from functools import reduce

type BoardT = List[List[str]]


class Solution:
    def solveNQueens(self, n: int) -> List[BoardT]:
        return solve(n)


def empty_board(n: int) -> BoardT:
    return [["." for _ in range(n)] for _ in range(n)]


def is_empty(b: BoardT) -> bool:
    acc = [[c == "." for c in row] for row in b]
    return all(chain.from_iterable(acc))


def is_complete(board: BoardT) -> bool:
    n = len(board)
    flat = chain.from_iterable(board)
    return reduce(lambda acc, x: acc + (1 if x == "Q" else 0), flat, 0) == n


def can_place(board: BoardT, row: int, col: int) -> bool:
    # check row
    if "Q" in board[row]:
        return False
    # check column
    for _row in board:
        if _row[col] == "Q":
            return False
    n = len(board)
    # check diagonals
    for i in range(n):
        j = col - (row - i)
        if 0 <= j < n and board[i][j] == "Q":
            return False
    for i in range(n):
        j = col + (row - i)
        if 0 <= j < n and board[i][j] == "Q":
            return False

    return True


def backtrack(board: BoardT, solutions: List[BoardT]):
    if is_complete(board):
        if board not in solutions:
            solutions.append(board)
        return True
    for i, row in enumerate(board):
        if "Q" in row:
            continue
        for j, _ in enumerate(row):
            if can_place(board, i, j):
                board[i][j] = "Q"
                backtrack(board, solutions)
                board[i][j] = "."


def solve(n: int):
    board = empty_board(n)
    solutions: List[BoardT] = []
    backtrack(board, solutions)
    strings = []
    for sol in solutions:
        _t = ["".join(row) for row in sol]
        strings.append(_t)
    return strings
