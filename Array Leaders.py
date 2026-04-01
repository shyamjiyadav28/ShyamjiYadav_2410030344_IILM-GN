class Solution:
    def leaders(self, arr):
        n = len(arr)
        result = []
        
        max_so_far = arr[-1]
        result.append(max_so_far)
        
        # Traverse from right
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_so_far:
                max_so_far = arr[i]
                result.append(arr[i])
        
        # Reverse to maintain order
        return result[::-1]
