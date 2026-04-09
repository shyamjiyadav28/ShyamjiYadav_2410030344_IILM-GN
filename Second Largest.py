class Solution:
    def getSecondLargest(self, arr):
        largest = float('-inf')
        second = float('-inf')

        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num > second and num != largest:
                second = num

        return second if second != float('-inf') else -1
