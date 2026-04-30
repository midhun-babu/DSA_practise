"""
LeetCode #5: Longest Palindromic Substring
Category: Dynamic Programming
Difficulty: Medium

Problem:
Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

LEARNING FOCUS:
- Expand around center technique
- DP on strings
- Palindrome properties
"""


def longest_palindrome_expand(s: str) -> str:
    
    if not s:
        return ""
    
    start = 0
    max_len = 0
    
    def expand_from_center(left: int, right: int) -> int:
        """Expand and return length of palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Odd length
        len1 = expand_from_center(i, i)
        # Even length
        len2 = expand_from_center(i, i + 1)
        
        current_len = max(len1, len2)
        if current_len > max_len:
            max_len = current_len
            start = i - (current_len - 1) // 2
    
    return s[start:start + max_len]


def longest_palindrome_dp(s: str) -> str:
    
    n = len(s)
    if n < 2:
        return s
    
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for lengths 3 and above
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
    ]
    
    for s, expected_options in test_cases:
        result = longest_palindrome_expand(s)
        print(f"s='{s}'")
        print(f"  Result: '{result}'")
        print(f"  Expected one of: {expected_options}")
        print(f"  {'✓ Pass' if result in expected_options else '✗ Fail'}")
        print()
