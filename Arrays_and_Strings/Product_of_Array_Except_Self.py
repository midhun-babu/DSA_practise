"""
LeetCode #238: Product of Array Except Self
Category: Arrays & Strings
Difficulty: Medium

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using division.

Example:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

LEARNING FOCUS:
- Prefix/Suffix product pattern
- Two-pass algorithm
- Space optimization
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    
    n = len(nums)
    answer = [1] * n
    
    # Left pass: fill in prefix products
    # answer[i] will hold product of all elements to the left of i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Right pass: multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
    ]
    
    for nums, expected in test_cases:
        result = product_except_self(nums)
        print(f"nums={nums}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
