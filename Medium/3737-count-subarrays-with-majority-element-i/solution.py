class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            freq = 0
            for j in range(i,len(nums)):
                if nums[j] == target:
                    freq += 1
                if freq > (j-i+1)//2:
                    count += 1

        return count
