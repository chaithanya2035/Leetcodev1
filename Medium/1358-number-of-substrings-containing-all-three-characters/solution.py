class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        d = {"a":-1,"b":-1,"c":-1}

        for i,c in enumerate(s):
            d[c] = i
            count += min(d["a"],d["b"],d["c"])+1

        return count
