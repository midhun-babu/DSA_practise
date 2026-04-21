"""
LeetCode #143: Reorder List
Category: Linked Lists
Difficulty: Medium

Problem:
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

Example:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

LEARNING FOCUS:
- Multiple techniques combined
- Find middle, reverse, merge
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


def reorder_list(head: Optional[ListNode]) -> None:
    
    if not head or not head.next:
        return
    
    # Step 1: Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    second = slow.next
    slow.next = None  # Split into two lists
    
    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    # Step 3: Merge alternately
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2


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
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [1, 2],
    ]
    
    for values in test_cases:
        head = create_list(values)
        print(f"Original: {head}")
        reorder_list(head)
        print(f"Reordered: {head}")
        print()
