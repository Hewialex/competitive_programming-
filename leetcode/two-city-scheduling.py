class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: -abs(x[0] - x[1]))
        b = a = len(costs)//2
        total = 0
        for aC,bC in costs:
            if b == 0 or (a > 0 and aC <= bC):
                total += aC
                a -= 1
            else:
                total += bC
                b -= 1
        return total