"""
LeetCode #217: Contains Duplicate
Category: Arrays & Strings
Difficulty: Easy

Problem:
Given an integer array nums, return true if any value appears at least twice,
and return false if every element is distinct.

Example:
Input: nums = [1, 2, 3, 1]
Output: true

LEARNING FOCUS:
- Hash Set for O(1) lookups
- Sorting approach as alternative
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains any duplicate.
    
    THE INTUITION:
    Use a set to track numbers we've seen. If we see a number again, 
    we found a duplicate!
    
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False


def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Alternative: Sort first, then check adjacent elements.
    
    Time: O(n log n) - sorting
    Space: O(1) - if in-place sort allowed
    """
    nums.sort()  # Sorts in-place
    
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    
    return False


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]
    
    for nums, expected in test_cases:
        result = contains_duplicate(nums[:])  # Copy for sort version
        print(f"nums={nums}")
        print(f"  Result: {result}, Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
