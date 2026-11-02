class Solution:
    def minMoves(self, nums: list[int]) -> int:
        ele = nums[0]
        c = 0
        for i in nums:
            if i == ele:
                c += 1

        if c == len(nums):
            return 0
        else:
            total = 0
            min_ele = min(nums)
            for i in nums:
                total += i - min_ele

            return total
