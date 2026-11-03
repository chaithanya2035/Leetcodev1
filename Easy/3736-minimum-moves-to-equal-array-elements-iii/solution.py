class Solution:
    def minMoves(self, nums: List[int]) -> int:
        c = 0
        ele = nums[0]
        for i in nums:
            if i == ele:
                c+= 1
        if c == len(nums):
            return 0
        else :
            max_ele = max(nums)
            total = 0

            for i in nums:
                total += max_ele - i

            return total
