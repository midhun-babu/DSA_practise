"""
LeetCode #10: Regular Expression Matching
Category: Dynamic Programming
Difficulty: Hard

Problem:
Given an input string s and a pattern p, implement regular expression matching.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.

LEARNING FOCUS:
- Complex DP with multiple cases
- Pattern matching
- State transitions
"""


def is_match(s: str, p: str) -> bool:
    
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns like a*, a*b* matching empty string
    for j in range(2, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Zero occurrences
                dp[i][j] = dp[i][j - 2]
                
                # One or more (if preceding element matches)
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            
            elif p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            
            else:
                dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
    
    return dp[m][n]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]
    
    for s, p, expected in test_cases:
        result = is_match(s, p)
        print(f"s='{s}', p='{p}'")
        print(f"  Match: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
