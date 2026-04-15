class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        
        freq = {}
        
        # Count elements in a
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        # Subtract counts using b
        for num in b:
            if num not in freq:
                return False
            freq[num] -= 1
            if freq[num] < 0:
                return False
        
        return True
