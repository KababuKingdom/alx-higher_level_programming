#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def is_safe(board, row, col, N):
    # Check if a given position is safe on the board
    # by checking the rows and diagonals
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

def nqueens(N, board=None, col=0):
    # Recursive function to find all solutions to the N queens problem
    if board is None:
        board = [[0 for _ in range(N)] for _ in range(N)]
    if col == N:
        for row in board:
            print(" ".join(str(x) for x in row))
        print()
        return
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            nqueens(N, board, col + 1)
            board[row][col] = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(N)
