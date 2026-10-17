class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_of_d = 0
        product = 1
        i = n
        while i > 0:
            sum_of_d += i%10
            product *= i%10
            i //= 10
        return n % (sum_of_d + product) == 0 
