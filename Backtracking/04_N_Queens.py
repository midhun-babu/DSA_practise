"""
LeetCode #51: N-Queens
Category: Backtracking
Difficulty: Hard

Problem:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Example:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

LEARNING FOCUS:
- Classic backtracking problem
- Constraint checking
- Diagonal tracking
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Sets to track attacked positions
    cols = set()
    diagonals = set()  # row - col (constant)
    anti_diagonals = set()  # row + col (constant)
    
    def backtrack(row: int):
        if row == n:
            # Found a solution
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            # Check if position is under attack
            if (col in cols or 
                (row - col) in diagonals or 
                (row + col) in anti_diagonals):
                continue
            
            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            
            # Recurse to next row
            backtrack(row + 1)
            
            # Backtrack
            board[row][col] = '.'
            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)
    
    backtrack(0)
    return result


# ============== TEST ==============
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"N = {n}")
    print(f"Number of solutions: {len(solutions)}")
    
    for i, solution in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        for row in solution:
            print(f"  {row}")
