"""
LeetCode #22: Generate Parentheses
Category: Backtracking
Difficulty: Medium

Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

LEARNING FOCUS:
- Constraint-based backtracking
- Tracking open/close counts
- Valid sequence generation
"""

from typing import List


def generate_parenthesis(n: int) -> List[str]:
    """
    Generate all valid parentheses combinations.
    
    THE INTUITION:
    We can add '(' if we haven't used all n opening parentheses.
    We can add ')' if we have more '(' than ')' so far.
    
    Time: O(4^n / sqrt(n)) - Catalan number
    Space: O(n)
    """
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Can add opening parenthesis
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Can add closing parenthesis
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result


# ============== TEST ==============
if __name__ == "__main__":
    for n in [1, 2, 3]:
        result = generate_parenthesis(n)
        print(f"n = {n}")
        print(f"Combinations ({len(result)} total):")
        for combo in result:
            print(f"  {combo}")
        print()
