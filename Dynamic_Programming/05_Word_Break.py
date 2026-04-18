"""
LeetCode #139: Word Break
Category: Dynamic Programming
Difficulty: Medium

Problem:
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times.

Example:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".

LEARNING FOCUS:
- String DP
- Prefix checking
- Bottom-up approach
"""

from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    
    word_set = set(word_dict)
    n = len(s)
    
    # dp[i] = True if s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can be segmented
    
    for i in range(1, n + 1):
        for j in range(i):
            # If s[0:j] can be segmented AND s[j:i] is a word
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ]
    
    for s, word_dict, expected in test_cases:
        result = word_break(s, word_dict)
        print(f"s='{s}', wordDict={word_dict}")
        print(f"  Can break: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
