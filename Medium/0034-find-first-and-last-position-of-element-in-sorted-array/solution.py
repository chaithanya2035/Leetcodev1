class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        if target not in nums or len(nums) == 0:
            return [-1,-1]
        a=[]
        a.append(nums.index(target))
        b=nums[::-1]
        x=(len(nums)-1)-(b.index(target))
        a.append(x)
        return a
