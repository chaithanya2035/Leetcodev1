class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i.lower()
        s2 = s1[::-1]
        return True if s1 == s2 else False
