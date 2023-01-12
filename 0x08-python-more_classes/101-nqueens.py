#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def nqueens(n, board=[]):
    if len(board) == n:
        print(board)
        return
    for col in range(n):
        board.append(col)
        if is_valid(board):
            nqueens(n, board)
        board.pop()

def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True

if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

nqueens(n)
