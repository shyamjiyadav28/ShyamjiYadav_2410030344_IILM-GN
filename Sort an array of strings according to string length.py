class Solution:
    def sortByLength(self, arr):
        arr.sort(key=len)   # sort based on length
        return arr
