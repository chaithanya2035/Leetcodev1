class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        x = len(temperatures)
        ans = [0]*x
        stack =[]
        for i in range(x):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i-prev
            stack.append(i)

        return ans
