"""
LeetCode #91: Decode Ways
Category: Dynamic Programming
Difficulty: Medium

Problem:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

Given a string s containing only digits, return the number of ways to decode it.

Example:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

LEARNING FOCUS:
- String DP with constraints
- Handling edge cases
- State transitions
"""


def num_decodings(s: str) -> int:
    """
    Count number of ways to decode string.
    
    THE INTUITION:
    dp[i] = number of ways to decode s[0:i]
    
    For each position, we can:
    1. Decode single digit (if s[i-1] != '0')
    2. Decode two digits (if 10 <= int(s[i-2:i]) <= 26)
    
    dp[i] = dp[i-1] (if single valid) + dp[i-2] (if double valid)
    
    Time: O(n)
    Space: O(1) - optimized
    """
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    
    # dp[i-2], dp[i-1], dp[i]
    prev2 = 1  # Empty string has 1 way
    prev1 = 1  # Single non-'0' digit has 1 way
    
    for i in range(2, n + 1):
        current = 0
        
        # Single digit decode (if current digit is not '0')
        if s[i - 1] != '0':
            current += prev1
        
        # Two digit decode (if 10 <= value <= 26)
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            current += prev2
        
        prev2 = prev1
        prev1 = current
    
    return prev1


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("12", 2),
        ("226", 3),
        ("0", 0),
        ("10", 1),
        ("27", 1),
    ]
    
    for s, expected in test_cases:
        result = num_decodings(s)
        print(f"s='{s}'")
        print(f"  Ways: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
