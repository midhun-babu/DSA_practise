"""
LeetCode #131: Palindrome Partitioning
Category: Backtracking
Difficulty: Medium

Problem:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

LEARNING FOCUS:
- Backtracking with palindrome check
- String partitioning
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    
    result = []
    
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]
    
    def backtrack(start: int, current: List[str]):
        if start == len(s):
            result.append(current[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()
    
    backtrack(0, [])
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = ["aab", "a", "efe"]
    
    for s in test_cases:
        result = partition(s)
        print(f"s = '{s}'")
        print(f"Partitions ({len(result)} total):")
        for p in result:
            print(f"  {p}")
        print()
