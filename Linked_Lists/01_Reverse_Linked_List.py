i"""
LeetCode #206: Reverse Linked List
Category: Linked Lists
Difficulty: Easy

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

LEARNING FOCUS:
- Pointer manipulation
- Iterative vs Recursive approaches
- In-place reversal
"""

from typing import Optional


class ListNode:
    """Node in a singly linked list."""
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


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    
    prev = None
    current = head
    
    while current:
        # Save next before we change current.next
        next_temp = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_temp
    
    return prev  # prev is now the new head


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    
    # Base case: empty or single node
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Put head at the end
    head.next.next = head
    head.next = None
    
    return new_head


# ============== HELPER ==============
def create_list(values: list) -> Optional[ListNode]:
    """Create linked list from Python list."""
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
        [1, 2, 3, 4, 5],
        [1, 2],
        [1],
        [],
    ]
    
    for values in test_cases:
        head = create_list(values)
        print(f"Original: {head}")
        reversed_head = reverse_list_iterative(head)
        print(f"Reversed: {reversed_head}")
        print()
