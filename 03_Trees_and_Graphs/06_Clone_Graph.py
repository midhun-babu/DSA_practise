"""
LeetCode #133: Clone Graph
Category: Trees & Graphs
Difficulty: Medium

Problem:
Given a reference of a node in a connected undirected graph, return a deep copy of the graph.

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]

LEARNING FOCUS:
- Graph traversal with tracking
- Hash map for visited nodes
- DFS/BFS for cloning
"""

from typing import Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """
    Clone graph using DFS.
    
    THE INTUITION:
    Use a hash map to track original node -> cloned node.
    Recursively clone neighbors and connect them.
    
    Time: O(V + E)
    Space: O(V)
    """
    if not node:
        return None
    
    old_to_new = {}
    
    def dfs(old_node: Node) -> Node:
        # Already cloned
        if old_node in old_to_new:
            return old_to_new[old_node]
        
        # Create clone
        new_node = Node(old_node.val)
        old_to_new[old_node] = new_node
        
        # Clone neighbors
        for neighbor in old_node.neighbors:
            new_node.neighbors.append(dfs(neighbor))
        
        return new_node
    
    return dfs(node)


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """
    Clone graph using BFS.
    
    Time: O(V + E)
    Space: O(V)
    """
    if not node:
        return None
    
    old_to_new = {node: Node(node.val)}
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in current.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            
            old_to_new[current].neighbors.append(old_to_new[neighbor])
    
    return old_to_new[node]


# ============== TEST ==============
if __name__ == "__main__":
    # Create graph: 1 -- 2
    #              |    |
    #              4 -- 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    
    cloned = clone_graph_dfs(node1)
    print(f"Original node val: {node1.val}")
    print(f"Cloned node val: {cloned.val}")
    print(f"Different objects: {node1 is not cloned}")  # Should be True
