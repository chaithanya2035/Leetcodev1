class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
         nums_set = set(nums)
         result = []
         min_num, max_num = min(nums),max(nums)
         for i in range(min_num,max_num):
            if i not in nums_set:
                result.append(i)

         return result
