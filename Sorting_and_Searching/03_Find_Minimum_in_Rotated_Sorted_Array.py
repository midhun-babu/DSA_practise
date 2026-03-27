"""
LeetCode #153: Find Minimum in Rotated Sorted Array
Category: Sorting & Searching
Difficulty: Medium

Problem:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element.

You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1

LEARNING FOCUS:
- Binary search for minimum
- Comparing with rightmost element
"""

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Find minimum in rotated sorted array.
    
    THE INTUITION:
    Compare middle with rightmost element:
    - If nums[mid] > nums[right]: Minimum is in right half
    - If nums[mid] < nums[right]: Minimum is in left half (including mid)
    - If equal (with duplicates): can't tell, shrink right
    
    Time: O(log n) for unique elements, O(n) worst with duplicates
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum is in right half
            left = mid + 1
        elif nums[mid] < nums[right]:
            # Minimum is in left half (could be mid itself)
            right = mid
        else:
            # Can't determine, shrink right
            right -= 1
    
    return nums[left]


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
    ]
    
    for nums, expected in test_cases:
        result = find_min(nums)
        print(f"nums={nums}")
        print(f"  Min: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
