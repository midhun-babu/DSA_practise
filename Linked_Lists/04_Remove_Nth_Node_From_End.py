"""
LeetCode #19: Remove Nth Node From End of List
Category: Linked Lists
Difficulty: Medium

Problem:
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

LEARNING FOCUS:
- Fast and Slow pointers
- One-pass algorithm
- Edge case handling
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
    dummy = ListNode(0, head)  # Dummy handles edge cases
    fast = slow = dummy
    
    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # slow.next is the node to remove
    slow.next = slow.next.next
    
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
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]
    
    for values, n, expected in test_cases:
        head = create_list(values)
        print(f"Original: {head}")
        result = remove_nth_from_end(head, n)
        print(f"After removing {n}th from end: {result}")
        print()
