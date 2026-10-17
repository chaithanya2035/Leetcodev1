class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                start_idx = end_idx
                end_idx = len(result)
            else:
                start_idx = 0
                end_idx = len(result)
            copy = list(result)
            for j in range(start_idx,end_idx):
                result.append(copy[j]+[nums[i]])

        return result
