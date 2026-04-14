"""
LeetCode #33: Search in Rotated Sorted Array
Category: Sorting & Searching
Difficulty: Medium

Problem:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.

Given the array nums after the rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

LEARNING FOCUS:
- Modified binary search
- Finding sorted half
- Handling rotation
"""

from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in left sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # Right half is sorted
        else:
            # Target is in right sorted half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1, 3], 3, 1),
    ]
    
    for nums, target, expected in test_cases:
        result = search_rotated(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"  Index: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
