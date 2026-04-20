class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        xor_all = 0
        xor_arr = 0

        for i in range(1, n + 1):
            xor_all ^= i

        for num in arr:
            xor_arr ^= num

        return xor_all ^ xor_arr 
