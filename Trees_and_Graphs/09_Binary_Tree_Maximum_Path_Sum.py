"""
LeetCode #124: Binary Tree Maximum Path Sum
Category: Trees & Graphs
Difficulty: Hard

Problem:
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
has an edge connecting them. A node can only appear in the sequence at most once.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: Path 15 -> 20 -> 7 has the maximum sum 42.

LEARNING FOCUS:
- Post-order traversal
- Global max tracking during recursion
- Path vs. subtree sums
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root: Optional[TreeNode]) -> int:
    
    max_sum = float('-inf')
    
    def max_gain(node: Optional[TreeNode]) -> int:
        """Returns max path sum starting from this node going downward."""
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Max gain from left and right (ignore negative contributions)
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Price of path going through this node (complete path)
        price_newpath = node.val + left_gain + right_gain
        
        # Update global max
        max_sum = max(max_sum, price_newpath)
        
        # Return max gain going upward (can only choose one branch)
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum


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
    
    root = create_tree([-10, 9, 20, None, None, 15, 7])
    print(f"Max path sum: {max_path_sum(root)}")  # 42
    
    root2 = create_tree([1, 2, 3])
    print(f"Max path sum: {max_path_sum(root2)}")  # 6
