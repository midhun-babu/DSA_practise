"""
LeetCode #104: Maximum Depth of Binary Tree
Category: Trees & Graphs
Difficulty: Easy

Problem:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

LEARNING FOCUS:
- Tree height calculation
- DFS recursion
- BFS level-order
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_dfs(root: Optional[TreeNode]) -> int:
    """
    Calculate max depth using DFS.
    
    THE INTUITION:
    Depth of tree = 1 + max(depth of left subtree, depth of right subtree)
    
    Time: O(n)
    Space: O(h)
    """
    if not root:
        return 0
    
    left_depth = max_depth_dfs(root.left)
    right_depth = max_depth_dfs(root.right)
    
    return 1 + max(left_depth, right_depth)


def max_depth_bfs(root: Optional[TreeNode]) -> int:
    """
    Calculate max depth using BFS (level-order).
    
    Count the number of levels.
    
    Time: O(n)
    Space: O(w)
    """
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth


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
    
    root = create_tree([3, 9, 20, None, None, 15, 7])
    print(f"DFS Depth: {max_depth_dfs(root)}")  # 3
    print(f"BFS Depth: {max_depth_bfs(root)}")  # 3
