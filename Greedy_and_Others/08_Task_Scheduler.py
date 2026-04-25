y"""
LeetCode #621: Task Scheduler
Category: Greedy & Others
Difficulty: Medium

Problem:
Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any order.
Each task is done in one unit of time. For each unit of time, the CPU could complete
either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between
two same tasks (the same letter in the array), that is that there must be at least n units
of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

LEARNING FOCUS:
- Greedy scheduling
- Counting and math
"""

from typing import List
from collections import Counter


def least_interval(tasks: List[str], n: int) -> int:
    
    if n == 0:
        return len(tasks)
    
    task_counts = Counter(tasks)
    max_count = max(task_counts.values())
    
    # Number of tasks with max frequency
    max_count_tasks = sum(1 for count in task_counts.values() if count == max_count)
    
    # Calculate minimum intervals needed
    part_count = max_count - 1
    part_length = n + 1
    empty_slots = part_count * (n + 1 - max_count_tasks)
    
    # Formula
    result = (max_count - 1) * (n + 1) + max_count_tasks
    
    # If we have more tasks than the formula accounts for
    return max(result, len(tasks))


# ============== TEST ==============
if __name__ == "__main__":
    test_cases = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ]
    
    for tasks, n, expected in test_cases:
        result = least_interval(tasks, n)
        print(f"tasks={tasks}, n={n}")
        print(f"  Min intervals: {result} (expected {expected})")
        print(f"  {'✓ Pass' if result == expected else '✗ Fail'}")
        print()
