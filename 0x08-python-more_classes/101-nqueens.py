#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def print_solution(board):
    """
    Prints the board configuration of a given solution
    """
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col):
    """
    Returns True if it is safe to place a queen at (row, col) on the board,
    False otherwise
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check if there is a queen in the same \ diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the same / diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(board, row):
    """
    Solves the N queens problem by trying to place a queen in every
    possible position in the current row and recursing to the next row
    """
    if row == len(board):
        print_solution(board)
        print()
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            solve_nqueens(board, row + 1)
            board[row][col] = "."

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [["." for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0)

if __name__ == "__main__":
    main()
