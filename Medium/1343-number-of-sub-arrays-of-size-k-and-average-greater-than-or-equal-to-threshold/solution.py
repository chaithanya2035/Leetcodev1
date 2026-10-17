class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold * k
        current = sum(arr[:k])
        count = 0
        if current >= target_sum :
            count += 1

        for i in range(k,len(arr)):
            current = current - arr[i-k] + arr[i]
            if  current >= target_sum:
                count += 1

        return count
