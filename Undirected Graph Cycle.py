from typing import List

class Solution:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        # DFS function
        def dfs(node, parent):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False

        # Check for all components
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True

        return False
