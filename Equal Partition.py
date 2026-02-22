class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        total = sum(arr)
        target = total // 2
        if n % 2 == 0:
            required_size = n // 2
        else:
            required_size = n // 2 
        
        result = []
        
        def backtrack(start, curr_subset, curr_sum):
           
            if len(curr_subset) == required_size and curr_sum == target:
                result.append(curr_subset[:])
                return True
            
            if curr_sum > target or len(curr_subset) > required_size:
                return False
            
            for i in range(start, n):
                curr_subset.append(arr[i])
                if backtrack(i + 1, curr_subset, curr_sum + arr[i]):
                    return True
                curr_subset.pop()
            
            return False
        
        backtrack(0, [], 0)
        
        subset1 = result[0]
        subset2 = arr[:]
        for num in subset1:
            subset2.remove(num)
        
        return [subset1, subset2]
