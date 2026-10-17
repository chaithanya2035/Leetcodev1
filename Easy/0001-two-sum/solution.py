class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        while(i<len(nums)):
            j=i+1
            while(j>i and j<len(nums)):
                if nums[i] + nums[j] == target:
                    return list((i,j))
                j += 1
            i += 1

sol = Solution()
List = []
target = None
print(sol.twoSum(List, target))
