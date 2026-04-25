"""
LeetCode #23: Merge k Sorted Lists
Category: Greedy & Others
Difficulty: Hard

Problem:
You are given an array of k linked-lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

LEARNING FOCUS:
- Min-heap for k-way merge
- Divide and conquer
"""

from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val
    
    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    lists = [lst for lst in lists if lst]
    
    if not lists:
        return None
    
    heap = []
    for i, node in enumerate(lists):
        heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, idx, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    
    return dummy.next


# ============== HELPER ==============
def create_list(values: list) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# ============== TEST ==============
if __name__ == "__main__":
    lists = [
        create_list([1, 4, 5]),
        create_list([1, 3, 4]),
        create_list([2, 6])
    ]
    
    result = merge_k_lists(lists)
    print(f"Merged: {result}")
