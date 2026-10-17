class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = k%len(nums)
        if not nums:
            return 
        if count == 0:
            return 
        
        nums[count:],nums[:count] = nums[:-count] , nums[-count:]


        
