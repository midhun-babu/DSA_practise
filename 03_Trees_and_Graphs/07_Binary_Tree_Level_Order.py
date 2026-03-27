"""
LeetCode #102: Binary Tree Level Order Traversal
Category: Trees & Graphs
Difficulty: Medium

Problem:
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

LEARNING FOCUS:
- BFS on trees
- Level-by-level processing
- Queue usage
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using BFS.
    
    THE INTUITION:
    Use a queue to process nodes level by level.
    For each level, process all nodes and add their children to queue.
    
    Time: O(n)
    Space: O(w) where w = max width of tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_values)
    
    return result


# ============== TEST ==============
if __name__ == "__main__":
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
    print(f"Level order: {level_order(root)}")
    # [[3], [9, 20], [15, 7]]
