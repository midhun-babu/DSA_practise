"""
LeetCode #215: Kth Largest Element in an Array
Category: Sorting & Searching
Difficulty: Medium

Problem:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

LEARNING FOCUS:
- QuickSelect algorithm
- Heap approach
- Partition technique
"""

from typing import List
import heapq
import random


def find_kth_largest_heap(nums: List[int], k: int) -> int:
    """
    Using min-heap of size k.
    
    THE INTUITION:
    Maintain a min-heap of k largest elements seen so far.
    The smallest in this heap is the kth largest overall.
    
    Time: O(n log k)
    Space: O(k)
    """
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    return min_heap[0]


def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    QuickSelect algorithm (Hoare's selection).
    
    THE INTUITION:
    Similar to QuickSort, but only recurse into one half.
    On average, this gives O(n) time.
    
    Time: O(n) average, O(n²) worst case
    Space: O(1)
    """
    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot_val = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        return store_idx
    
    def quickselect(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]
        
        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)
        
        if k_smallest == pivot_idx:
            return nums[k_smallest]
        elif k_smallest < pivot_idx:
            return quickselect(left, pivot_idx - 1, k_smallest)
        else:
            return quickselect(pivot_idx + 1, right, k_smallest)
    
    # kth largest = (n-k)th smallest (0-indexed)
    return quickselect(0, len(nums) - 1, len(nums) - k)


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
    ]
    
    for nums, k, expected in test_cases:
        result_heap = find_kth_largest_heap(nums[:], k)
        result_qs = find_kth_largest_quickselect(nums[:], k)
        print(f"nums={nums}, k={k}")
        print(f"  Heap: {result_heap}, QuickSelect: {result_qs}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result_heap == expected and result_qs == expected else '✗ Fail'}")
        print()
