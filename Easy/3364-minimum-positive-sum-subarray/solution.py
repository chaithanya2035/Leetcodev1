class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        arr=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                k=nums[i:j+1]
                if l <= len(k) <= r:
                    q=(sum(k))
                    if q >0:
                        arr.append(q)
        if len(arr)==0:
            return -1
        return min(arr)
