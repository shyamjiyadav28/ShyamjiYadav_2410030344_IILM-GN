class Solution:
    def isBalanced(self, s):
        stack = []
        
        # mapping of closing → opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            # if opening bracket → push
            if ch in "({[":
                stack.append(ch)
            else:
                # if stack empty OR mismatch
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        # if stack empty → balanced
        return len(stack) == 0
