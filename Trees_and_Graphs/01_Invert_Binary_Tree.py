"""
LeetCode #226: Invert Binary Tree
Category: Trees & Graphs
Difficulty: Easy

Problem:
Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

LEARNING FOCUS:
- Tree traversal (DFS/BFS)
- Recursion on trees
- Swapping nodes
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree_recursive(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert binary tree using DFS recursion.
    
    THE INTUITION:
    For each node, swap its left and right children, then recursively invert both subtrees.
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack, h = tree height
    """
    if not root:
        return None
    
    # Swap left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree_recursive(root.left)
    invert_tree_recursive(root.right)
    
    return root


def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Invert using BFS (level-order).
    
    Time: O(n)
    Space: O(w) - w = max width of tree
    """
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# ============== HELPER ==============
def create_tree(values: list) -> Optional[TreeNode]:
    """Create tree from level-order list."""
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


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert tree to level-order list."""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None
    while result and result[-1] is None:
        result.pop()
    
    return result


# ============== TEST ==============
if __name__ == "__main__":
    root = create_tree([4, 2, 7, 1, 3, 6, 9])
    print(f"Original: {tree_to_list(root)}")
    inverted = invert_tree_recursive(root)
    print(f"Inverted: {tree_to_list(inverted)}")
