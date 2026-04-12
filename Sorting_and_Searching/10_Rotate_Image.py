"""
LeetCode #48: Rotate Image
Category: Sorting & Searching
Difficulty: Medium

Problem:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

LEARNING FOCUS:
- Matrix transformation
- Transpose + Reverse pattern
- Layer-by-layer rotation
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


# ============== TEST ==============
if __name__ == "__main__":
    def print_matrix(m):
        for row in m:
            print(row)
    
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
    ]
    
    for matrix in test_cases:
        print("Original:")
        print_matrix(matrix)
        rotate(matrix)
        print("Rotated:")
        print_matrix(matrix)
        print()
