class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp = n
        lis = []
        x = 0 
        sum = 0
        while temp != 0:
            i = temp%10
            if i != 0:
                lis.append(i)
                sum += i
            temp = temp//10


        for i in range(len(lis)-1,-1,-1):
            x = x*10 + lis[i]

        return x * sum
