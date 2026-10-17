from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = Counter(s)
        dic2 = Counter(t)

        for i in dic1:
            if i in dic2:
                if dic1[i] != dic2[i]:
                    return False
            else:
                return False
        return True
