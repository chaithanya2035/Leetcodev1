class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = {}
        d1 = {}

        for ch in target:
            d[ch] = s.count(ch)
            d1[ch] = target.count(ch)

        count = float('inf')
        for key in d.keys():
            if d[key] < d1[key]:
                return 0
            count = min(count,d[key]//d1[key])

        return count
