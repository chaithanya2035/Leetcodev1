class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        results = [[]]
        for i in nums:
            for j in list(results):
                results.append(j+[i])

        return results
