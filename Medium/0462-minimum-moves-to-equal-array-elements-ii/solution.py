class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        c = 0
        ele = nums[0]
        for i in nums:
            if ele == i:
                c += 1
            
        if c == len(nums):
            return 0
        else:
            nums.sort()
            mid = len(nums)//2
            total = 0
            for i in range(mid):
                total += nums[mid] - nums[i]
            for i in range(mid+1,len(nums)):
                total += nums[i] - nums[mid]

            return total 
