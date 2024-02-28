class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        for i in range(0,rowIndex + 1):
            cur = [1] * (i+1)
            for j in range(1,i):
                cur[j] = prev[j-1] + prev[j]
            prev = cur
        return cur
