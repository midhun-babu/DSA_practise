"""
LeetCode #239: Sliding Window Maximum
Category: Greedy & Others
Difficulty: Hard

Problem:
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

LEARNING FOCUS:
- Monotonic deque
- Sliding window optimization
"""

from typing import List
from collections import deque


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    
    if not nums or k == 0:
        return []
    
    result = []
    dq = deque()  # Store indices, values in decreasing order
    
    for i, num in enumerate(nums):
        # Remove elements smaller than current (they can't be max)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Remove elements out of window
        if dq[0] < i - k + 1:
            dq.popleft()
        
        # Add to result once window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
    ]
    
    for nums, k, expected in test_cases:
        result = max_sliding_window(nums, k)
        print(f"nums={nums}, k={k}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
