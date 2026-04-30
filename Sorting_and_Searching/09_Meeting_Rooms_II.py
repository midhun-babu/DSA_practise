"""
LeetCode #253: Meeting Rooms II
Category: Sorting & Searching
Difficulty: Medium

Problem:
Given an array of meeting time intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

LEARNING FOCUS:
- Chronological ordering
- Min-heap for tracking end times
- Sweep line algorithm
"""

from typing import List
import heapq


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min-heap of end times
    end_times = [intervals[0][1]]
    
    for start, end in intervals[1:]:
        # If earliest ending meeting is done, reuse that room
        if start >= end_times[0]:
            heapq.heappop(end_times)
        
        # Schedule current meeting
        heapq.heappush(end_times, end)
    
    return len(end_times)


def min_meeting_rooms_sweep(intervals: List[List[int]]) -> int:
    
    if not intervals:
        return 0
    
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    
    rooms = 0
    end_ptr = 0
    
    for start in starts:
        if start >= ends[end_ptr]:
            # A meeting ended, reuse room
            end_ptr += 1
        else:
            # Need new room
            rooms += 1
    
    return rooms


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[0, 30], [5, 10], [10, 15], [15, 20]], 2),
    ]
    
    for intervals, expected in test_cases:
        result_heap = min_meeting_rooms(intervals)
        result_sweep = min_meeting_rooms_sweep(intervals)
        print(f"intervals={intervals}")
        print(f"  Heap: {result_heap}, Sweep: {result_sweep}")
        print(f"  Expected: {expected}")
        print(f"  {'✓ Pass' if result_heap == expected and result_sweep == expected else '✗ Fail'}")
        print()
