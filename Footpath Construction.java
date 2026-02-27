class Solution {

    public int[] createFootpath(int n, int m, int[][] a, int q, int[][] queries) {

        int[] result = new int[q];

        for (int k = 0; k < q; k++) {

            int r = queries[k][0] - 1;   // convert to 0-based
            int c = queries[k][1] - 1;

            int sum = 0;

            // Top-left
            if (r > 0 && c > 0) {
                int min = Integer.MAX_VALUE;
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        min = Math.min(min, a[i][j]);
                    }
                }
                sum += min;
            }

            // Top-right
            if (r > 0 && c < m - 1) {
                int min = Integer.MAX_VALUE;
                for (int i = 0; i < r; i++) {
                    for (int j = c + 1; j < m; j++) {
                        min = Math.min(min, a[i][j]);
                    }
                }
                sum += min;
            }

            // Bottom-left
            if (r < n - 1 && c > 0) {
                int min = Integer.MAX_VALUE;
                for (int i = r + 1; i < n; i++) {
                    for (int j = 0; j < c; j++) {
                        min = Math.min(min, a[i][j]);
                    }
                }
                sum += min;
            }

            // Bottom-right
            if (r < n - 1 && c < m - 1) {
                int min = Integer.MAX_VALUE;
                for (int i = r + 1; i < n; i++) {
                    for (int j = c + 1; j < m; j++) {
                        min = Math.min(min, a[i][j]);
                    }
                }
                sum += min;
            }

            result[k] = sum;
        }

        return result;
    }
}
