#!/usr/bin/python3

import sys


def solve_nqueens(N):
    # Check if N is an integer
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Helper function to check if a queen can be placed at the given position
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i] == col:
                return False

        # Check if there is a queen in the upper-left diagonal
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i] == j:
                return False
            i -= 1
            j -= 1

        # Check if there is a queen in the upper-right diagonal
        i = row - 1
        j = col + 1
        while i >= 0 and j < N:
            if board[i] == j:
                return False
            i -= 1
            j += 1

        return True

    # Helper function to recursively solve the N Queens problem
    def solve(board, row):
        # Base case: all queens have been placed
        if row == N:
            print_solution(board)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    # Helper function to print the solution
    def print_solution(board):
        solution = [[i, board[i]] for i in range(N)]
        print(solution)

    # Initialize the board
    board = [-1] * N

    # Solve the N Queens problem
    solve(board, 0)


# Check if the program is called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command-line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Solve the N Queens problem
solve_nqueens(N)
