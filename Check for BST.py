class Solution:
    def isBST(self, root):
        
        def check(node, low, high):
            if not node:
                return True
            
            # value must be strictly between low and high
            if node.data <= low or node.data >= high:
                return False
            
            # check left and right subtree
            return (check(node.left, low, node.data) and
                    check(node.right, node.data, high))
        
        return check(root, float('-inf'), float('inf'))
