class Solution:
    def maxProfit(self, x, y, a, b):
        n = len(a)

        # Store tasks with profit difference
        tasks = []

        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))

        # Sort by descending difference
        tasks.sort(reverse=True)

        profit = 0

        for diff, pa, pb in tasks:

            # Prefer machine giving higher profit
            if (pa >= pb and x > 0) or y == 0:
                profit += pa
                x -= 1
            else:
                profit += pb
                y -= 1

        return profit
