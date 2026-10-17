class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        run_sum = 0 
        max_sum = max(nums)
        for i in nums:
            run_sum += i
            max_sum = max(max_sum,run_sum)
            if run_sum < 0:
                run_sum = 0
        return max_sum
