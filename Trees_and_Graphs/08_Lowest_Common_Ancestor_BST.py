"""
LeetCode #235: Lowest Common Ancestor of a Binary Search Tree
Category: Trees & Graphs
Difficulty: Easy

Problem:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants.

Example:
Input: root = [6,2,8,0,4,7,9], p = 2, q = 8
Output: 6

LEARNING FOCUS:
- BST properties (left < root < right)
- Efficient traversal using BST property
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in a BST.
    
    THE INTUITION:
    In a BST:
    - All values in left subtree are smaller than root
    - All values in right subtree are larger than root
    
    If p.val <= root.val <= q.val (or vice versa), root is the LCA!
    If both are smaller, go left. If both are larger, go right.
    
    Time: O(h) where h = tree height
    Space: O(1)
    """
    current = root
    
    while current:
        # Both values are greater, LCA is in right subtree
        if p.val > current.val and q.val > current.val:
            current = current.right
        
        # Both values are smaller, LCA is in left subtree
        elif p.val < current.val and q.val < current.val:
            current = current.left
        
        # Found the split point - this is the LCA
        else:
            return current
    
    return None


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
    
    def find_node(root, val):
        current = root
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None
    
    root = create_tree([6, 2, 8, 0, 4, 7, 9])
    p = find_node(root, 2)
    q = find_node(root, 8)
    lca = lowest_common_ancestor(root, p, q)
    print(f"LCA of 2 and 8: {lca.val}")  # 6
    
    p2 = find_node(root, 2)
    q2 = find_node(root, 4)
    lca2 = lowest_common_ancestor(root, p2, q2)
    print(f"LCA of 2 and 4: {lca2.val}")  # 2
