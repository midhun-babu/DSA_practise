"""
LeetCode #62: Unique Paths
Category: Dynamic Programming
Difficulty: Medium

Problem:
There is a robot on an m x n grid. The robot is initially located at the top-left corner.
The robot tries to move to the bottom-right corner. The robot can only move either down or right.

Given the two integers m and n, return the number of possible unique paths.

Example:
Input: m = 3, n = 7
Output: 28

LEARNING FOCUS:
- 2D grid DP
- Combinatorics alternative
- Space optimization
"""


def unique_paths(m: int, n: int) -> int:
    
    # dp[j] = number of ways to reach current row's column j
    dp = [1] * n  # First row: all 1s (only one way - go right)
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j - 1]
    
    return dp[n - 1]


def unique_paths_math(m: int, n: int) -> int:
    """
    Math solution using combinations.
    
    THE INTUITION:
    Robot needs to make (m-1) down moves and (n-1) right moves.
    Total moves = (m-1) + (n-1) = m + n - 2
    
    Number of unique paths = C(m+n-2, m-1) = (m+n-2)! / ((m-1)! × (n-1)!)
    
    Time: O(min(m, n))
    Space: O(1)
    """
    import math
    return math.comb(m + n - 2, m - 1)


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        (3, 7, 28),
        (3, 2, 3),
        (7, 3, 28),
        (3, 3, 6),
    ]
    
    for m, n, expected in test_cases:
        result_dp = unique_paths(m, n)
        result_math = unique_paths_math(m, n)
        print(f"m={m}, n={n}")
        print(f"  DP: {result_dp}, Math: {result_math}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result_dp == expected and result_math == expected else '✗ Fail'}")
        print()
