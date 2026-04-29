class Solution:
    def reverseWords(self, s):   # ✅ add self
        # Step 1: split by dots
        parts = s.split('.')
        
        # Step 2: remove empty strings
        words = [word for word in parts if word]
        
        # Step 3: reverse words
        words.reverse()
        
        # Step 4: join with single dot
        return '.'.join(words)
