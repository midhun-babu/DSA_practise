"""
LeetCode #435: Non-overlapping Intervals
Category: Sorting & Searching
Difficulty: Medium

Problem:
Given an array of intervals where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest non-overlapping.

Example:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest are non-overlapping.

LEARNING FOCUS:
- Greedy algorithm
- Sorting by end time
- Activity selection problem
"""

from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Minimum intervals to remove to make non-overlapping.
    
    THE INTUITION (Greedy):
    Sort by end time. Always keep the interval that ends earliest!
    This leaves more room for subsequent intervals.
    
    Time: O(n log n)
    Space: O(1) or O(n) depending on sort
    """
    if not intervals:
        return 0
    
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = float('-inf')
    
    for interval in intervals:
        if interval[0] >= end:
            # No overlap, keep this interval
            end = interval[1]
        else:
            # Overlap, remove this interval
            count += 1
    
    return count


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]
    
    for intervals, expected in test_cases:
        result = erase_overlap_intervals(intervals)
        print(f"intervals={intervals}")
        print(f"  To remove: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
