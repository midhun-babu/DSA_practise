"""
LeetCode #300: Longest Increasing Subsequence
Category: Dynamic Programming
Difficulty: Medium

Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], length 4.

LEARNING FOCUS:
- DP with binary search optimization
- Patience sorting technique
- LIS pattern
"""

from typing import List
import bisect


def length_of_lis_dp(nums: List[int]) -> int:

    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Each element is LIS of length 1 by itself
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def length_of_lis_binary_search(nums: List[int]) -> int:
    
    tails = []  # tails[i] = smallest tail of LIS with length i+1
    
    for num in nums:
        # Find position where num should be inserted
        idx = bisect.bisect_left(tails, num)
        
        if idx == len(tails):
            tails.append(num)  # Extend longest subsequence
        else:
            tails[idx] = num  # Replace to get smaller tail
    
    return len(tails)


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]
    
    for nums, expected in test_cases:
        result_dp = length_of_lis_dp(nums)
        result_bs = length_of_lis_binary_search(nums)
        print(f"nums={nums}")
        print(f"  DP: {result_dp}, Binary Search: {result_bs}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result_dp == expected and result_bs == expected else '✗ Fail'}")
        print()
