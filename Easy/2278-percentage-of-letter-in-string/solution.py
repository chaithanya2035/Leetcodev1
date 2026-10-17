class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((float(s.count(letter))/len(s))*100)
