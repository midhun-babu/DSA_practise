"""
LeetCode #141: Linked List Cycle
Category: Linked Lists
Difficulty: Easy

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle, otherwise return false.

Example:
Input: head = [3,2,0,-4], pos = 1 (tail connects to node at index 1)
Output: true

LEARNING FOCUS:
- Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
- Fast and Slow pointers
- O(1) space cycle detection
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next  # Start fast one step ahead
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True


def has_cycle_hash_set(head: Optional[ListNode]) -> bool:
    """
    Alternative: Use hash set to track visited nodes.
    
    Time: O(n)
    Space: O(n)
    """
    visited = set()
    current = head
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    
    return False


# ============== TEST ==============
if __name__ == "__main__":
    # Create list with cycle: 3 -> 2 -> 0 -> -4 -> back to 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle
    
    print("List with cycle:", has_cycle(node1))  # True
    
    # List without cycle
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_a.next = node_b
    
    print("List without cycle:", has_cycle(node_a))  # False
