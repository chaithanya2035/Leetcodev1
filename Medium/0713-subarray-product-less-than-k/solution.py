
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        count = 0
        prod = 1
        j = 0

        for i in range(len(nums)):
            prod *= nums[i]

            while prod >= k and j <= i:
                prod = prod // nums[j]
                j += 1

            count += i - j + 1

        return count
