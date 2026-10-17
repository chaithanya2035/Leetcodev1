class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        visit = set(nums)
        max_multiple = max(nums)
        for i in range(1,max_multiple+k):
            if i%k == 0:
                if i not in visit:
                    return i
        else:
            return max_multiple+k
