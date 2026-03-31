class Solution:
    def search(self, txt, pat):
        n, m = len(txt), len(pat)
        
        if m > n:
            return False
        
        pat_count = [0] * 26
        window_count = [0] * 26
        
        for ch in pat:
            pat_count[ord(ch) - ord('a')] += 1
        
        for i in range(m):
            window_count[ord(txt[i]) - ord('a')] += 1
        
        if window_count == pat_count:
            return True
        
        for i in range(m, n):
            window_count[ord(txt[i]) - ord('a')] += 1
            window_count[ord(txt[i - m]) - ord('a')] -= 1
            
            if window_count == pat_count:
                return True
        
        return Falsea
