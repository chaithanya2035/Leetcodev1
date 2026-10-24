class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if j > i and prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices
