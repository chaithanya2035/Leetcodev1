class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == right-left-nums[i]:
                return i
            left += nums[i]
        else:
            return -1
