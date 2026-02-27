class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        col0 = 1  # To track whether first column should be zero
        
        # Step 1: Use first row and first column as markers
        for i in range(m):
            
            if matrix[i][0] == 0:
                col0 = 0
                
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row
                    matrix[0][j] = 0  # mark column
        
        # Step 2: Traverse from bottom to avoid overwriting markers
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            
            if col0 == 0:
                matrix[i][0] = 0
