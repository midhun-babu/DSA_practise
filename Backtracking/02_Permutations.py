"""
LeetCode #46: Permutations
Category: Backtracking
Difficulty: Medium

Problem:
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

LEARNING FOCUS:
- Backtracking with used array
- Permutation generation
- Swapping technique
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    
    result = []
    n = len(nums)
    used = [False] * n
    
    def backtrack(current: List[int]):
        if len(current) == n:
            result.append(current[:])
            return
        
        for i in range(n):
            if not used[i]:
                # Use nums[i]
                used[i] = True
                current.append(nums[i])
                
                backtrack(current)
                
                # Backtrack
                current.pop()
                used[i] = False
    
    backtrack([])
    return result


def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    Alternative: Use swapping (no extra used array).
    
    Time: O(n × n!)
    Space: O(n) - recursion stack
    """
    result = []
    n = len(nums)
    
    def backtrack(start: int):
        if start == n:
            result.append(nums[:])
            return
        
        for i in range(start, n):
            # Swap start and i
            nums[start], nums[i] = nums[i], nums[start]
            
            backtrack(start + 1)
            
            # Backtrack (swap back)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result


# ============== TEST ==============
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = permute(nums)
    print(f"nums = {nums}")
    print(f"Permutations ({len(result)} total):")
    for p in result:
        print(f"  {p}")
