class Solution:
    def binarysearch(self, arr, k):
        left, right = 0, len(arr) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == k:
                ans = mid
                right = mid - 1   # move left for first occurrence
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1

        return ans
