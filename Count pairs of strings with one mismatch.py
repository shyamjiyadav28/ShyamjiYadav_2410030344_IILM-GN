from collections import defaultdict

class Solution:
    def countPairs(self, arr):
        pattern_count = defaultdict(int)
        char_count = defaultdict(lambda: defaultdict(int))

        for s in arr:
            for i in range(len(s)):
                pattern = s[:i] + '*' + s[i+1:]
                pattern_count[pattern] += 1
                char_count[pattern][s[i]] += 1

        ans = 0

        for pattern in pattern_count:
            total = pattern_count[pattern]
            ans += total * (total - 1) // 2

            for freq in char_count[pattern].values():
                ans -= freq * (freq - 1) // 2

        return ans
