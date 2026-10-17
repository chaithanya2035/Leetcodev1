from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        min_value = min(freq.values())
        index = 0
        if min_value>1:
            return -1
        for i in freq:
            if freq[i] == min_value:
                index = s.index(i)
                break
        return index
