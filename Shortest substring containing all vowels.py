class Solution:
    def substrWithVowels(self, s1, s2):
        required = set(s1)
        freq = {}
        formed = 0
        required_count = len(required)

        left = 0
        min_len = float('inf')

        for right in range(len(s2)):
            char = s2[right]

            if char in required:
                freq[char] = freq.get(char, 0) + 1
                if freq[char] == 1:
                    formed += 1

            while formed == required_count:
                min_len = min(min_len, right - left + 1)

                left_char = s2[left]
                if left_char in required:
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        formed -= 1

                left += 1

        return min_len if min_len != float('inf') else -1
