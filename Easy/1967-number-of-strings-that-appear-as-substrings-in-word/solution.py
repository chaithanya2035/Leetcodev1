class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for w in patterns if w in word)
