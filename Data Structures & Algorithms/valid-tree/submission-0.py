class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # a tree must have (n-1) edges
        if len(edges) != n-1:
            return False
        
        neighbors = {i: [] for i in range(n)}

        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        visited = set()

        # dfs guarantees no cycles are detected
        def dfs(node, parent):
            visited.add(node)

            for neighbor in neighbors[node]:

                if neighbor == parent:
                    continue
                
                if neighbor in visited: # "i found a cycle"
                    return False
                
                if not dfs(neighbor, node): # "my child found a cycle, so i must report it too!"
                    return False
                
            return True
    
        return dfs(0, -1) and len(visited) == n
        # len(visited) == n gurantees that every node is reachable

# Time: O(V + E)
# - Build adjacency list: O(V + E)
# - DFS visits each vertex and examines each edge: O(V + E)

# Space: O(V + E)
# - Adjacency list: O(V + E) stores both vertices and edges
# - Visited set: O(V)
# - Recursive call stack: O(V) worst case