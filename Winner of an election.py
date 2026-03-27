class Solution:
    def winner(self, arr):
        freq = {}
        
        # Count votes
        for name in arr:
            freq[name] = freq.get(name, 0) + 1
        
        max_votes = 0
        winner_name = ""
        
        # Find winner
        for name in freq:
            if freq[name] > max_votes:
                max_votes = freq[name]
                winner_name = name
            elif freq[name] == max_votes:
                winner_name = min(winner_name, name)
        
        return [winner_name, str(max_votes)]
