class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n   # handle d > n
        
        # helper function to reverse array
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Step 1: reverse first d elements
        reverse(0, d - 1)
        
        # Step 2: reverse remaining elements
        reverse(d, n - 1)
        
        # Step 3: reverse whole array
        reverse(0, n - 1)
        
        return arr
