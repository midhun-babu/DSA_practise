"""
LeetCode #15: 3Sum
Category: Arrays & Strings
Difficulty: Medium

Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

LEARNING FOCUS:
- Sorting + Two Pointers
- Skipping duplicates
- Reducing O(n³) to O(n²)
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    THE INTUITION:
    1. Sort the array first
    2. For each number, use two pointers to find pairs that sum to its negative
    
    Why sorting helps:
    - Skip duplicates easily
    - Two pointers can find pairs in O(n) instead of O(n²)
    
    Time: O(n²) - sorting + nested loops
    Space: O(1) or O(n) depending on sort
    """
    result = []
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers for remaining two numbers
        left, right = i + 1, n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            
            elif current_sum < target:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum
    
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, 3, 4, 5], []),
    ]
    
    for nums, expected in test_cases:
        result = three_sum(nums)
        print(f"nums={nums}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
