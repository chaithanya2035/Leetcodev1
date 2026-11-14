class Solution:
    def calculate(self,n,dp):
        if n == 1 or n == 0 :
            dp[n] = n
            return dp[n]
        
        if dp[n]!= -1:
            return dp[n]

        dp[n] = self.calculate(n-1,dp) + self.calculate(n-2,dp)

        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+2)

        return self.calculate(n+1,dp)
    
