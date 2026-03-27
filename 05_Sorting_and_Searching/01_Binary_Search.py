"""
LeetCode #704: Binary Search
Category: Sorting & Searching
Difficulty: Easy

Problem:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

LEARNING FOCUS:
- Binary search pattern
- Finding boundaries
- Avoiding infinite loops
"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Binary search for target in sorted array.
    
    THE INTUITION:
    Repeatedly divide the search space in half.
    - If target == middle, found it!
    - If target < middle, search left half
    - If target > middle, search right half
    
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(nums: List[int], target: int) -> int:
    """
    Recursive version.
    
    Time: O(log n)
    Space: O(log n) - recursion stack
    """
    def search(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return search(mid + 1, right)
        else:
            return search(left, mid - 1)
    
    return search(0, len(nums) - 1)


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
    ]
    
    for nums, target, expected in test_cases:
        result = binary_search(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"  Index: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
