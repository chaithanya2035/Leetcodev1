class Solution:
    def reverse(self, x: int) -> int:
        n = str(x)
        if n[0] == "-":
            f = int("-"+n[:0:-1])
        else:
            f = int(n[::-1])

        if (-2**31) < f < (2**31):
            return f
        else:
            return 0

