"""
LeetCode #200: Number of Islands
Category: Trees & Graphs
Difficulty: Medium

Problem:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Example:
Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
Output: 1

LEARNING FOCUS:
- Graph traversal on grid
- DFS/BFS for connected components
- Flood fill algorithm
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    """
    Count islands using DFS.
    
    THE INTUITION:
    Scan through grid. When we find land ('1'), we found a new island!
    Use DFS to "sink" (mark as visited) all connected land.
    
    Time: O(m × n)
    Space: O(m × n) - recursion stack in worst case
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r: int, c: int):
        """Sink the entire island starting from (r, c)."""
        # Check bounds
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        # If water or already visited
        if grid[r][c] == '0':
            return
        
        # Sink this cell
        grid[r][c] = '0'
        
        # Sink neighbors (4-directional)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)  # Sink entire island
    
    return count


# ============== TEST ==============
if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(f"Grid 1: {num_islands([row[:] for row in grid1])} islands")  # 1
    
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(f"Grid 2: {num_islands([row[:] for row in grid2])} islands")  # 3
