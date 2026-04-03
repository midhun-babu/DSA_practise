"""
LeetCode #53: Maximum Subarray (Kadane's Algorithm)
Category: Arrays & Strings
Difficulty: Medium

Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.

LEARNING FOCUS:
- Kadane's Algorithm
- Dynamic Programming on arrays
- Greedy decision making
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    
    # Current maximum sum ending at current position
    current_sum = nums[0]
    
    # Global maximum sum found so far
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Decision: extend previous or start fresh?
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update global maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_with_indices(nums: List[int]) -> tuple:
    """
    Also return the subarray indices.
    
    Returns: (max_sum, start_index, end_index)
    """
    current_sum = nums[0]
    max_sum = nums[0]
    current_start = 0
    max_start = max_end = 0
    
    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            # Start fresh
            current_sum = nums[i]
            current_start = i
        else:
            # Extend
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = current_start
            max_end = i
    
    return max_sum, max_start, max_end


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3], -1),
    ]
    
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f"nums={nums}")
        print(f"  Result: {result}, Expected: {expected}")
        
        # Also show the subarray
        total, start, end = max_subarray_with_indices(nums)
        print(f"  Subarray: nums[{start}:{end+1}] = {nums[start:end+1]}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
