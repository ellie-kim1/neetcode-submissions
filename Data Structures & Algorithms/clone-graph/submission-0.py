"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        copies = {}

        # edge case: empty Node
        if node is None:
            return None

        def dfs(node):

            if node in copies:
                return copies[node]
            
            copy = Node(node.val)
            copies[node] = copy

            for neighbor in node.neighbors:
                copied_neighbor = dfs(neighbor)
                copy.neighbors.append(copied_neighbor)
            
            return copy
        
        return dfs(node)

        