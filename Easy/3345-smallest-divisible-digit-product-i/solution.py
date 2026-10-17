class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            product = (i // 10) * (i % 10) if i >= 10 else i

            if product % t == 0:
                return i
