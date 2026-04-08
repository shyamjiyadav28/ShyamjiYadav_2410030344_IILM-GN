class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # Expected sums
        S = n * (n + 1) // 2
        S2 = n * (n + 1) * (2*n + 1) // 6
        
        # Actual sums
        actual_sum = sum(arr)
        actual_square_sum = sum(x*x for x in arr)
        
        # Equations
        diff = S - actual_sum              # x - y
        square_diff = S2 - actual_square_sum  # x^2 - y^2
        
        sum_xy = square_diff // diff      # x + y
        
        # Solve
        x = (diff + sum_xy) // 2          # missing
        y = x - diff                     # repeating
        
        return [y, x]   # [repeating, missing]
