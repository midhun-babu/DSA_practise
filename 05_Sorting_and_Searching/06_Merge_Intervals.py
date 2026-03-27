"""
LeetCode #56: Merge Intervals
Category: Sorting & Searching
Difficulty: Medium

Problem:
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, merge them into [1,6].

LEARNING FOCUS:
- Sorting by start time
- Greedy merging
- Interval problems pattern
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.
    
    THE INTUITION:
    1. Sort intervals by start time
    2. Iterate and merge overlapping intervals
    
    Two intervals overlap if: current.start <= previous.end
    
    Time: O(n log n) - sorting
    Space: O(n) - for result
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if overlapping
        if current[0] <= last[1]:
            # Merge by extending the end
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 4]], [[0, 4]]),
    ]
    
    for intervals, expected in test_cases:
        result = merge(intervals)
        print(f"intervals={intervals}")
        print(f"  Merged: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
