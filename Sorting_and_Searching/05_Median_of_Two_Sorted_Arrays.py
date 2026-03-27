"""
LeetCode #4: Median of Two Sorted Arrays
Category: Sorting & Searching
Difficulty: Hard

Problem:
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

LEARNING FOCUS:
- Binary search on partitions
- Finding correct split point
- Edge case handling
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find median using binary search on partitions.
    
    THE INTUITION:
    We need to partition both arrays such that:
    - Left side has equal (or one more) elements than right
    - All elements in left <= all elements in right
    
    Binary search on the smaller array to find the correct partition.
    
    Time: O(log(min(m, n)))
    Space: O(1)
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    total_left = (m + n + 1) // 2
    
    left, right = 0, m
    
    while left <= right:
        i = (left + right) // 2  # Partition in nums1
        j = total_left - i       # Partition in nums2
        
        nums1_left = nums1[i - 1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        
        nums2_left = nums2[j - 1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')
        
        # Check if we found the correct partition
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Correct partition!
            if (m + n) % 2 == 1:
                return max(nums1_left, nums2_left)
            else:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        
        elif nums1_left > nums2_right:
            # Too many elements from nums1 in left
            right = i - 1
        else:
            # Too few elements from nums1 in left
            left = i + 1
    
    raise ValueError("Input arrays not sorted")


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ]
    
    for nums1, nums2, expected in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        print(f"nums1={nums1}, nums2={nums2}")
        print(f"  Median: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
