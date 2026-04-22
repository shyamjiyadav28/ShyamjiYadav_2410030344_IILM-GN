from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)                # number of vertices
        visited = [False] * V
        result = []
        
        q = deque()
        q.append(0)
        visited[0] = True
        
        while q:
            node = q.popleft()
            result.append(node)
            
            # traverse neighbors in given order
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        
        return result
