class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = []
        product = 1
        for i in nums:
            left.append(product)
            product *= i

        product = 1
        right = []
        for i in range(n-1,-1,-1):
            right.append(product)
            product *= nums[i]

        result = []
        for i in range(n):
            result.append(left[i]*right[n-i-1])

        return result

            
