class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        dp = [0]*n
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if not stack:
                dp[i] = n - i
            else:
                dp[i] = stack[-1] - i
            
            stack.append(i)
        
        return sum(dp)
