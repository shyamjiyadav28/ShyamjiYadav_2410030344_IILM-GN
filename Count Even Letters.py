class Solution:
    def count(self, s):
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = 0
        for val in freq.values():
            if val % 2 == 0:
                ans += 1

        return ans
