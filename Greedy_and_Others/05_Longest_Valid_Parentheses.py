"""
LeetCode #32: Longest Valid Parentheses
Category: Greedy & Others
Difficulty: Hard

Problem:
Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses substring.

Example:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

LEARNING FOCUS:
- Stack-based tracking
- DP approach
- Two-pass approach
"""


def longest_valid_parentheses_stack(s: str) -> int:
    
    stack = [-1]  # Base index
    max_len = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            
            if not stack:
                stack.append(i)  # New base
            else:
                max_len = max(max_len, i - stack[-1])
    
    return max_len


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()(()", 4),
    ]
    
    for s, expected in test_cases:
        result = longest_valid_parentheses_stack(s)
        print(f"s='{s}': {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
