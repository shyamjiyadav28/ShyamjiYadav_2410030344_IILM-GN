class Solution(object):
    def ispoweroftwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
n = int(input("Enter a number: "))
obj = Solution()
result = obj.ispoweroftwo(n)

print("Is power of two:", result)