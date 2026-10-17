class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for _ in nums:
            if _ in s:
                return _
            s.add(_)
