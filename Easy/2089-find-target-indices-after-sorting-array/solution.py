class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        s_l,t=sorted(nums),len(nums)
        count=[]
        for i in range(t):
            if s_l[i] == target:
                count.append(i)
        return count
