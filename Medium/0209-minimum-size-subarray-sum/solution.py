class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")

        if sum(nums) < target:
            return 0

        i = j = 0
        current = 0
        for j in range(len(nums)):
            current += nums[j]
            while current >= target:
                min_len = min(min_len,j-i
                +1)
                current -= nums[i]
                i+=1

        return min_len
