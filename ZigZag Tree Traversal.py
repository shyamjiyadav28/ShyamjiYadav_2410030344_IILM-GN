from collections import deque

class Solution:
    def zigZagTraversal(self, root):
        
        result = []
        
        if not root:
            return result
        
        q = deque()
        q.append(root)
        
        left_to_right = True
        
        while q:
            
            size = len(q)
            level = [0] * size
            
            for i in range(size):
                
                node = q.popleft()
                
                # Correct index based on direction
                if left_to_right:
                    index = i
                else:
                    index = size - i - 1
                
                level[index] = node.data
                
                # Add children
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            # Add level to result
            result.extend(level)
            
            # Change direction
            left_to_right = not left_to_right
        
        return result
