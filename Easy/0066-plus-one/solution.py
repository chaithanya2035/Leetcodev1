class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_of_digits = 0

        for i in digits:
            sum_of_digits = sum_of_digits*10 + i

        sum_of_digits += 1

        result = []

        while sum_of_digits > 0:
            result.append(sum_of_digits%10)
            sum_of_digits = sum_of_digits//10

        return result[::-1]
