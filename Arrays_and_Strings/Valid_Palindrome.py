"""
LeetCode #125: Valid Palindrome
Category: Arrays & Strings
Difficulty: Easy

Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

LEARNING FOCUS:
- Two Pointers from both ends
- Character filtering
- Case-insensitive comparison
"""


def is_palindrome(s: str) -> bool:
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


def is_palindrome_simple(s: str) -> bool:
    """
    Simpler approach: clean string first, then check.
    
    Time: O(n)
    Space: O(n) - for cleaned string
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
    ]
    
    for s, expected in test_cases:
        result = is_palindrome(s)
        print(f"s='{s}'")
        print(f"  Result: {result}, Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
