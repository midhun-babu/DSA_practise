"""
LeetCode #42: Trapping Rain Water
Category: Greedy & Others
Difficulty: Hard

Problem:
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

LEARNING FOCUS:
- Two pointers
- Precompute max heights
- Water level calculation
"""

from typing import List


def trap_two_pointers(height: List[int]) -> int:
    
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 1, 1], 0),
    ]
    
    for height, expected in test_cases:
        result = trap_two_pointers(height)
        print(f"height={height}")
        print(f"  Water: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
