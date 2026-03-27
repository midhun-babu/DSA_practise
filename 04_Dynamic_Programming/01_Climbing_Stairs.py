"""
LeetCode #70: Climbing Stairs
Category: Dynamic Programming
Difficulty: Easy

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1

LEARNING FOCUS:
- Fibonacci pattern in DP
- Bottom-up vs Top-down
- Space optimization
"""


def climb_stairs(n: int) -> int:
    """
    Count ways to climb n stairs.
    
    THE INTUITION:
    To reach step n, you could have come from:
    - Step n-1 (took 1 step)
    - Step n-2 (took 2 steps)
    
    So: ways[n] = ways[n-1] + ways[n-2] (Fibonacci!)
    
    Time: O(n)
    Space: O(1) - optimized version
    """
    if n <= 2:
        return n
    
    # Only need to track last two values
    prev2 = 1  # ways to reach n-2
    prev1 = 2  # ways to reach n-1
    
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def climb_stairs_dp_array(n: int) -> int:
    """
    Full DP array approach (easier to understand).
    
    Time: O(n)
    Space: O(n)
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
    ]
    
    for n, expected in test_cases:
        result = climb_stairs(n)
        print(f"n={n}: {result} ways (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
