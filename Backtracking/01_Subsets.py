"""
LeetCode #78: Subsets
Category: Backtracking
Difficulty: Medium

Problem:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

LEARNING FOCUS:
- Backtracking template
- Decision tree
- Include/Exclude pattern
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    
    result = []
    
    def backtrack(start: int, current: List[int]):
        # Add current subset to result
        result.append(current[:])
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Include nums[i]
            current.append(nums[i])
            
            # Recurse
            backtrack(i + 1, current)
            
            # Backtrack (exclude nums[i])
            current.pop()
    
    backtrack(0, [])
    return result


# ============== TEST ==============
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"nums = {nums}")
    print(f"Subsets ({len(result)} total):")
    for subset in result:
        print(f"  {subset}")
