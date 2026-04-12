class Solution:
    def getPairs(self, arr):
        arr.sort()
        left = 0
        right = len(arr) - 1
        result = []

        while left < right:
            s = arr[left] + arr[right]

            if s == 0:
                result.append([arr[left], arr[right]])

                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

        return result
