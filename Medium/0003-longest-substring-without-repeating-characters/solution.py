class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                n = max(n,j-i+1)

        return n
