"""
LeetCode #37: Sudoku Solver
Category: Backtracking
Difficulty: Hard

Problem:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.

The '.' character indicates empty cells.

LEARNING FOCUS:
- Complex backtracking
- Constraint propagation
- Board state management
"""

from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Solve Sudoku puzzle in-place.
    
    THE INTUITION:
    Find empty cells and try digits 1-9.
    Check if digit is valid in that position.
    If valid, place it and recurse. If solution found, return True.
    If no digit works, backtrack.
    
    Time: O(9^(n*n)) worst case
    Space: O(n*n)
    """
    def is_valid(row: int, col: int, num: str) -> bool:
        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False
        
        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        
        return True
    
    def backtrack() -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num
                            
                            if backtrack():
                                return True
                            
                            board[row][col] = '.'  # Backtrack
                    
                    return False  # No valid number found
        
        return True  # All cells filled
    
    backtrack()


# ============== TEST ==============
if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    print("Before:")
    for row in board:
        print(row)
    
    solve_sudoku(board)
    
    print("\nAfter:")
    for row in board:
        print(row)
