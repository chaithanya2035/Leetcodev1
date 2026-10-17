class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        index = float('-inf')
        for i, j in enumerate(nums):
            if j == target:
                found = True
                index = i
        return index if found else -1
