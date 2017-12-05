class NumMatrix(object):
    # beats 83.86%
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in xrange(1, len(row)):
                row[col] += row[col - 1]
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col - 1]

        diff = original - val

        for y in xrange(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for x in xrange(row1, row2 + 1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1 - 1]
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)