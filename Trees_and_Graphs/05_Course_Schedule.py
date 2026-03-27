"""
LeetCode #207: Course Schedule
Category: Trees & Graphs
Difficulty: Medium

Problem:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

LEARNING FOCUS:
- Directed graph cycle detection
- Topological sort (Kahn's algorithm)
- DFS with state tracking
"""

from typing import List
from collections import deque, defaultdict


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Check if all courses can be finished (no circular dependencies).
    
    THE INTUITION (Topological Sort - Kahn's Algorithm):
    1. Build graph and count in-degrees (number of prerequisites)
    2. Start with courses that have no prerequisites
    3. "Take" courses and reduce in-degrees of dependent courses
    4. If we can take all courses, no cycle exists
    
    Time: O(V + E)
    Space: O(V + E)
    """
    # Build adjacency list and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Start with courses having no prerequisites
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
    courses_taken = 0
    
    while queue:
        current = queue.popleft()
        courses_taken += 1
        
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    return courses_taken == num_courses


def can_finish_dfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Alternative: DFS with cycle detection.
    
    States: 0 = unvisited, 1 = visiting, 2 = visited
    If we encounter a node being visited, there's a cycle.
    
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses
    
    def has_cycle(node: int) -> bool:
        if state[node] == 1:
            return True  # Cycle detected!
        if state[node] == 2:
            return False  # Already processed
        
        state[node] = 1  # Mark as visiting
        
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        
        state[node] = 2  # Mark as visited
        return False
    
    for i in range(num_courses):
        if state[i] == 0:
            if has_cycle(i):
                return False
    
    return True


# ============== TEST ==============
if __name__ == "__main__":
    print(f"Test 1: {can_finish(2, [[1, 0]])}")  # True
    print(f"Test 2: {can_finish(2, [[1, 0], [0, 1]])}")  # False (cycle)
    print(f"Test 3: {can_finish_dfs(4, [[1, 0], [2, 1], [3, 2]])}")  # True
