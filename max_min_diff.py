class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def isPossible(mid):
            count = 1
            last = arr[0]
            
            for i in range(1, len(arr)):
                if arr[i] - last >= mid:
                    count += 1
                    last = arr[i]
                    if count == k:
                        return True
            return False
        
        low = 1
        high = arr[-1] - arr[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
