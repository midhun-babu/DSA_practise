"""
LeetCode #20: Valid Parentheses
Category: Greedy & Others
Difficulty: Easy

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

LEARNING FOCUS:
- Stack for matching
- LIFO pattern
"""


def is_valid(s: str) -> bool:
    
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching:
            # Closing bracket
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
    ]
    
    for s, expected in test_cases:
        result = is_valid(s)
        print(f"s='{s}': {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
