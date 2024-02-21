class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix),len(matrix[0])
        self.prefix = [[0] * m for _ in range(n)]
        self.prefix[0][0] = matrix[0][0]
        for i in range(1,m):
            self.prefix[0][i] = self.prefix[0][i-1] + matrix[0][i]
        for j in range(1,n):
            self.prefix[j][0] = self.prefix[j-1][0] + matrix[j][0]
        for i in range(1,m):
            for j in range(1,n):
                self.prefix[j][i] = self.prefix[j][i-1] + self.prefix[j-1][i]- self.prefix[j-1][i-1]  + matrix[j][i]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        else:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1 -1][col2] + self.prefix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)