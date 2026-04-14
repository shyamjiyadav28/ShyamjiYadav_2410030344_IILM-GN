class Solution:
    def minPlatform(self, arr, dep):
        arr.sort()
        dep.sort()
        
        n = len(arr)
        i = 0
        j = 0
        
        platforms_needed = 0
        max_platforms = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:
                platforms_needed -= 1
                j += 1
                
        return max_platforms
