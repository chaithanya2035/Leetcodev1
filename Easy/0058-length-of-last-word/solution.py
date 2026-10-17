class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        return len(s1.split(" ")[-1])
