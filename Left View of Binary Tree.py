from collections import deque

class Solution:
    def leftView(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                
                # First node of each level
                if i == 0:
                    result.append(node.data)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
