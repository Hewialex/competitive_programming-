class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = []
        colMax = []
        total = 0
        for i in range(len(grid)):
            rowMax.append(max(grid[i]))
        for j in range(len(grid[0])):
            max_cur = -inf
            for i in range(len(grid)):
                max_cur = max(max_cur , grid[i][j])
            colMax.append(max_cur)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(rowMax[i],colMax[j]) - grid[i][j]
        return total


