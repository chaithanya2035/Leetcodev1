class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a, b):
            a, b = abs(a), abs(b)
            while b != 0:
                a, b = b, a % b
            return a

        even= list(range(2, 2 * n + 1, 2))
        odd= list(range(1, 2 * n, 2))

        return gcd(sum(even),sum(odd))
