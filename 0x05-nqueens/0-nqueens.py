#!/usr/bin/python3
"""solves N-queens puzzle"""
import sys

def is_safe(board, row, col, N):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def solve_nqueens_util(board, row, N, solutions):
    if row == N:
        solutions.append(board[:])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row] = -1

def solve_nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [-1] * N
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print_solution(solution)

def print_solution(solution):
    print("[", end="")
    for i in range(len(solution)):
        print([i, solution[i]], end="")
        if i != len(solution) - 1:
            print(", ", end="")
    print("]")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    solve_nqueens(N)
