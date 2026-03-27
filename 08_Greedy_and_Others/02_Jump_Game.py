"""
LeetCode #55: Jump Game
Category: Greedy & Others
Difficulty: Medium

Problem:
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

LEARNING FOCUS:
- Greedy approach
- Track maximum reachable
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    Check if last index is reachable.
    
    THE INTUITION (Greedy):
    Track the furthest index we can reach.
    If at any point, current index > max_reach, we can't proceed.
    
    Time: O(n)
    Space: O(1)
    """
    max_reach = 0
    
    for i, jump in enumerate(nums):
        # If we can't reach this index, return False
        if i > max_reach:
            return False
        
        # Update furthest reachable
        max_reach = max(max_reach, i + jump)
    
    return True


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 1, 1, 1], True),
    ]
    
    for nums, expected in test_cases:
        result = can_jump(nums)
        print(f"nums={nums}")
        print(f"  Can jump: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
