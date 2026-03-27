"""
LeetCode #1: Two Sum
Category: Arrays & Strings
Difficulty: Easy

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

LEARNING FOCUS:
- Hash Map pattern for O(1) lookups
- Trading space for time
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target.
    
    THE INTUITION:
    As we walk through the array, we ask: "Have I seen the number that would 
    complete this pair before?" We use a hash map to remember what we've seen.
    
    Time: O(n) - single pass
    Space: O(n) - hash map storage
    """
    # This dictionary stores: {number_we_saw: its_index}
    # Think of it as our "memory" of numbers we've passed by
    seen = {}
    
    for i, num in enumerate(nums):
        # What number do we need to reach the target?
        needed = target - num
        
        # Have we seen this needed number before?
        if needed in seen:
            return [seen[needed], i]
        
        # Remember this number and where we found it
        seen[num] = i
    
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - check every pair.
    
    Time: O(n²) - nested loops
    Space: O(1) - no extra space
    
    This is what you might do first, then optimize to the hash map solution.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"nums={nums}, target={target}")
        print(f"  Result: {result}, Expected: {expected}")
        print(f"  ✓ Pass" if result == expected else f"  ✗ Fail")
        print()
