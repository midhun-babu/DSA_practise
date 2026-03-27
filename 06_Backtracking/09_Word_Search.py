"""
LeetCode #79: Word Search
Category: Backtracking
Difficulty: Medium

Problem:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

LEARNING FOCUS:
- 2D grid backtracking
- Direction arrays
- In-place marking
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Check if word exists in board.
    
    THE INTUITION:
    For each cell, try to match word starting from there.
    Mark visited cells and backtrack if path fails.
    
    Time: O(m × n × 4^L) where L = len(word)
    Space: O(L) - recursion stack
    """
    if not board or not board[0]:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(r: int, c: int, index: int) -> bool:
        # Found all characters
        if index == len(word):
            return True
        
        # Check bounds and match
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False
        
        # Mark as visited (in-place)
        temp = board[r][c]
        board[r][c] = '#'
        
        # Try all 4 directions
        found = (backtrack(r + 1, c, index + 1) or
                 backtrack(r - 1, c, index + 1) or
                 backtrack(r, c + 1, index + 1) or
                 backtrack(r, c - 1, index + 1))
        
        # Backtrack (restore)
        board[r][c] = temp
        
        return found
    
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    
    return False


# ============== TEST ==============
if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    
    test_cases = [
        ("ABCCED", True),
        ("SEE", True),
        ("ABCB", False),
    ]
    
    for word, expected in test_cases:
        # Create fresh copy of board
        board_copy = [row[:] for row in board]
        result = exist(board_copy, word)
        print(f"word = '{word}'")
        print(f"  Found: {result}, Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
