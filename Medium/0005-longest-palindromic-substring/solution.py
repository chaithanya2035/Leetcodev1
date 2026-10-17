class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0

        def expand(left,right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            odd = expand(i,i)
            even = expand(i,i+1)

            current_len = max(odd,even)

            if current_len > max_len:
                max_len = current_len
                start = i - (current_len-1)//2

        return s[start:start+max_len]
