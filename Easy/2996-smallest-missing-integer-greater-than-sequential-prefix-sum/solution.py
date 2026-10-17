class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        i = 1 
        n = len(nums)

        while i < n and (nums[i] == nums[i-1]+1) :
            i += 1
        
        sequence_sum = sum(nums[:i])

        num_set = set(nums)

        x = sequence_sum

        while x in num_set:
            x += 1

        return x
