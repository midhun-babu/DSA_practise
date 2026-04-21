"""
LeetCode #21: Merge Two Sorted Lists
Category: Linked Lists
Difficulty: Easy

Problem:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list by splicing together the nodes.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

LEARNING FOCUS:
- Two pointers on linked lists
- Dummy node technique
- In-place merging
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


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = list1 if list1 else list2
    
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
        ([1, 2, 4], [1, 3, 4]),
        ([], [0]),
        ([], []),
    ]
    
    for v1, v2 in test_cases:
        l1 = create_list(v1)
        l2 = create_list(v2)
        print(f"list1: {l1}")
        print(f"list2: {l2}")
        merged = merge_two_lists(l1, l2)
        print(f"merged: {merged}")
        print()
