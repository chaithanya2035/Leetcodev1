class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        else :
            result = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
            return abs(max(result))
