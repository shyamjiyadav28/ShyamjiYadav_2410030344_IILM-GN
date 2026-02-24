import java.util.*;

class Solution {
    
    public ArrayList<Long> submatrixSum(long[][] a, int n, int m, int[][] query, int q) {
        
        // Step 1: Build Prefix Matrix
        long[][] prefix = new long[n][m];
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                
                prefix[i][j] = a[i][j];
                
                if(i > 0)
                    prefix[i][j] += prefix[i-1][j];
                
                if(j > 0)
                    prefix[i][j] += prefix[i][j-1];
                
                if(i > 0 && j > 0)
                    prefix[i][j] -= prefix[i-1][j-1];
            }
        }
        
        // Step 2: Process Queries
        ArrayList<Long> result = new ArrayList<>();
        
        for(int k = 0; k < q; k++) {
            
            int r1 = query[k][0];
            int c1 = query[k][1];
            int r2 = query[k][2];
            int c2 = query[k][3];
            
            long total = prefix[r2][c2];
            
            if(r1 > 0)
                total -= prefix[r1-1][c2];
            
            if(c1 > 0)
                total -= prefix[r2][c1-1];
            
            if(r1 > 0 && c1 > 0)
                total += prefix[r1-1][c1-1];
            
            result.add(total);
        }
        
        return result;
    }
}
