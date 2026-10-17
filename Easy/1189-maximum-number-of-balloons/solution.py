class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d ={}
        d1={}
        s = "balloon"
        for ch in s:
            d[ch] = text.count(ch)
            d1[ch] = s.count(ch)
        
        count = float('inf')
        for key in d1.keys():
            if d[key] < d1[key]:
                return 0
            count = min(count,d[key]//d1[key])

        return count
