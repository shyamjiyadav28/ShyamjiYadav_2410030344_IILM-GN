class Solution:
    def longestSubarray(self, arr, k):   # ✅ add self
        mp = {}
        prefix_sum = 0
        max_len = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                max_len = i + 1
            
            if (prefix_sum - k) in mp:
                max_len = max(max_len, i - mp[prefix_sum - k])
            
            if prefix_sum not in mp:
                mp[prefix_sum] = i
        
        return max_len
