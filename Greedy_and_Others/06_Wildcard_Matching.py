"""
LeetCode #44: Wildcard Matching
Category: Greedy & Others
Difficulty: Hard

Problem:
Given an input string s and a pattern p, implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string.

LEARNING FOCUS:
- Two pointers with backtracking
- Greedy matching
- DP alternative
"""


def is_match(s: str, p: str) -> bool:
    """
    Wildcard matching with two pointers.
    
    THE INTUITION:
    Use two pointers. When '*' encountered, remember position.
    If matching fails later, backtrack and try matching one more char with '*'.
    
    Time: O(n × m) worst case, often O(n + m)
    Space: O(1)
    """
    s_len, p_len = len(s), len(p)
    s_idx = p_idx = 0
    star_idx = -1
    s_tmp_idx = -1
    
    while s_idx < s_len:
        if p_idx < p_len and (p[p_idx] == '?' or p[p_idx] == s[s_idx]):
            s_idx += 1
            p_idx += 1
        elif p_idx < p_len and p[p_idx] == '*':
            star_idx = p_idx
            s_tmp_idx = s_idx
            p_idx += 1
        elif star_idx == -1:
            return False
        else:
            # Backtrack: '*' matches one more character
            p_idx = star_idx + 1
            s_tmp_idx += 1
            s_idx = s_tmp_idx
    
    # Check remaining pattern - all must be '*'
    while p_idx < p_len and p[p_idx] == '*':
        p_idx += 1
    
    return p_idx == p_len


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
    ]
    
    for s, p, expected in test_cases:
        result = is_match(s, p)
        print(f"s='{s}', p='{p}': {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
