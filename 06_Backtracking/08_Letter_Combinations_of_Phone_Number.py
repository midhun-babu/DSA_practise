"""
LeetCode #17: Letter Combinations of a Phone Number
Category: Backtracking
Difficulty: Medium

Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations
that the number could represent. Return the answer in any order.

Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

LEARNING FOCUS:
- Digit to letter mapping
- Multiple choice backtracking
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    """
    Generate all letter combinations for phone number.
    
    THE INTUITION:
    For each digit, try all possible letters it represents.
    
    Time: O(4^n) where n = len(digits), 4 is max letters per digit
    Space: O(n)
    """
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index: int, current: str):
        if index == len(digits):
            result.append(current)
            return
        
        digit = digits[index]
        for letter in phone_map[digit]:
            backtrack(index + 1, current + letter)
    
    backtrack(0, "")
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = ["23", "", "2"]
    
    for digits in test_cases:
        result = letter_combinations(digits)
        print(f"digits = '{digits}'")
        print(f"Combinations ({len(result)} total):")
        for combo in result:
            print(f"  {combo}")
        print()
