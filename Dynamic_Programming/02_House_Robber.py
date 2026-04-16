"""
LeetCode #198: House Robber
Category: Dynamic Programming
Difficulty: Medium

Problem:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. The only constraint stopping you
from robbing each of them is that adjacent houses have security systems connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money=2), rob house 3 (money=9), rob house 5 (money=1).
Total = 2 + 9 + 1 = 12.

LEARNING FOCUS:
- Decision making at each step
- DP state transition
- Space optimization
"""

from typing import List


def rob(nums: List[int]) -> int:
  
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]  # Max up to house i-2
    prev1 = max(nums[0], nums[1])  # Max up to house i-1
    
    for i in range(2, len(nums)):
        current = max(prev1, nums[i] + prev2)
        prev2 = prev1
        prev1 = current
    
    return prev1


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
    ]
    
    for nums, expected in test_cases:
        result = rob(nums)
        print(f"nums={nums}")
        print(f"  Max: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
