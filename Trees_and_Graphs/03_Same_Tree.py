"""
LeetCode #100: Same Tree
Category: Trees & Graphs
Difficulty: Easy

Problem:
Given the roots of two binary trees p and q, write a function to check if they are the same.
Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: true

LEARNING FOCUS:
- Tree comparison
- Recursive structure matching
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two trees are identical.
    
    THE INTUITION:
    Two trees are the same if:
    1. Both are None (base case)
    2. Both have same root value AND left subtrees are same AND right subtrees are same
    
    Time: O(n)
    Space: O(h)
    """
    # Both empty
    if not p and not q:
        return True
    
    # One empty, one not
    if not p or not q:
        return False
    
    # Both non-empty: check values and recurse
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))


# ============== TEST ==============
if __name__ == "__main__":
    from collections import deque
    
    def create_tree(values):
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root
    
    p = create_tree([1, 2, 3])
    q = create_tree([1, 2, 3])
    print(f"Same tree: {is_same_tree(p, q)}")  # True
    
    p2 = create_tree([1, 2])
    q2 = create_tree([1, None, 2])
    print(f"Different structure: {is_same_tree(p2, q2)}")  # False
