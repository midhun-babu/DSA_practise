"""
LeetCode #76: Minimum Window Substring
Category: Arrays & Strings
Difficulty: Hard

Problem:
Given two strings s and t, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

LEARNING FOCUS:
- Sliding Window with constraints
- Two pointers with validation
- Character frequency counting
"""

from collections import Counter, defaultdict


def min_window(s: str, t: str) -> str:
    
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters needed from t
    required = Counter(t)
    required_count = len(t)
    
    min_len = float('inf')
    min_start = 0
    left = 0
    
    for right in range(len(s)):
        # Expand window
        if s[right] in required:
            if required[s[right]] > 0:
                required_count -= 1
            required[s[right]] -= 1
        
        # Contract window while valid
        while required_count == 0:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_start = left
            
            # Remove leftmost character
            if s[left] in required:
                required[s[left]] += 1
                if required[s[left]] > 0:
                    required_count += 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]
    
    for s, t, expected in test_cases:
        result = min_window(s, t)
        print(f"s='{s}', t='{t}'")
        print(f"  Result: '{result}', Expected: '{expected}'")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
