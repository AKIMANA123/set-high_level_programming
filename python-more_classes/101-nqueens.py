#!/usr/bin/python3
"""
N Queens puzzle solver using backtracking
"""

import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]

    Args:
        board: The current board state
        row: Row to check
        col: Column to check
        n: Size of the board

    Returns:
        True if safe, False otherwise
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens_util(board, col, n, solutions):
    """Solve N Queens using backtracking

    Args:
        board: The current board state
        col: Current column to place queen
        n: Size of the board
        solutions: List to store solutions

    Returns:
        True if solution found, False otherwise
    """
    if col >= n:
        # Convert board to solution format
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions

    Args:
        n: Size of the board
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


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

    solve_nqueens(N)
