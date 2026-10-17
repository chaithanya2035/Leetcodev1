class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        w = str(x)
        r_w = w[::-1]
        return True if int(r_w) == x else False  
          
sol = Solution()
x = 121
print(sol.isPalindrome(x))
