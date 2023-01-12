#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def solve_nqueens(n):
    def is_safe(board, row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def backtrack(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    solutions = []
    board = [-1] * n
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
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
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
