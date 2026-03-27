"""
LeetCode #57: Insert Interval
Category: Sorting & Searching
Difficulty: Medium

Problem:
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi]
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

LEARNING FOCUS:
- Three-phase approach
- Finding overlap boundaries
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Insert and merge new interval.
    
    THE INTUITION (Three phases):
    1. Add all intervals ending before new_interval starts
    2. Merge all overlapping intervals with new_interval
    3. Add all intervals starting after new_interval ends
    
    Time: O(n)
    Space: O(n)
    """
    result = []
    i = 0
    n = len(intervals)
    
    new_start, new_end = new_interval
    
    # Phase 1: Add all intervals before new_interval
    while i < n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1
    
    # Phase 2: Merge all overlapping intervals
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    
    result.append([new_start, new_end])
    
    # Phase 3: Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
    ]
    
    for intervals, new_interval, expected in test_cases:
        result = insert(intervals, new_interval)
        print(f"intervals={intervals}, newInterval={new_interval}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
