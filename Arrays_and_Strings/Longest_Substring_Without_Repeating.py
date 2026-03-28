"""
LeetCode #3: Longest Substring Without Repeating Characters
Category: Arrays & Strings
Difficulty: Medium

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

LEARNING FOCUS:
- Sliding Window pattern
- Hash Set for O(1) lookups
- Window expansion and contraction
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters.
    
    THE INTUITION (Sliding Window):
    We maintain a window [left, right] that contains no repeating characters.
    - Expand by moving 'right' pointer
    - When we find a duplicate, shrink from 'left' until valid again
    
    Time: O(n) - each character visited at most twice
    Space: O(min(m, n)) where m = charset size
    """
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If duplicate found, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to window
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length


def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized version using hash map to store indices.
    
    Instead of shrinking one by one, we jump 'left' directly.
    
    Time: O(n)
    Space: O(min(m, n))
    """
    char_index = {}  # char -> last seen index
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If we've seen this char AND it's inside current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Jump left to exclude previous occurrence
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]
    
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        print(f"s='{s}'")
        print(f"  Result: {result}, Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
