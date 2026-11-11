class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        sep= need1 *cost1 + need2 * cost2

        mixed = max(need1,need2)*costBoth

        if (need1 > need2):
            min_req = costBoth*need2+(need1-need2)*cost1
        else:
            min_req = costBoth*need1+(need2-need1)*cost2

        return min(sep,mixed,min_req)
