class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        target = num
        low = 0
        high = target//2
        while low <= high :
            mid = low + (high-low)//2
            squre = mid * mid 
            if squre == num:
                return True
            elif squre > num:
                high = mid -1
            else:
                low = mid + 1
            
        return False
