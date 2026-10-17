class Solution:
    def countCommas(self, n: int) -> int:
        total_count = 0
        threshold = 1000

        while n >= threshold:
            count = (n - threshold) + 1
            total_count += count

            threshold *= 1000

        return total_count
