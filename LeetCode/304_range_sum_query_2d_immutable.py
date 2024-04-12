class NumMatrix:
    """
    https://www.youtube.com/watch?v=KE8MQuwE2yA
    
    beats 96.04%
    """
    def __init__(self, matrix):
        self.sum_ = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.sum_[i][j + 1]
                self.sum_[i + 1][j + 1] = previous + above

    def sumRegion(self, row1, col1, row2, col2):
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sum_[r2][c2]
        above = self.sum_[r1 -1][c2]
        left = self.sum_[r2][c1 - 1]
        topLeft = self.sum_[r1 -1][c1 - 1]
        return bottomRight - above - left + topLeft

class NumMatrixV1:
    """
    beats 89.40%
    """
    def __init__(self, matrix):
        self.sum_ = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.sum_[i][j + 1]
                self.sum_[i + 1][j + 1] = previous + above

    def sumRegion(self, row1, col1, row2, col2):
        sum_col2 = self.sum_[row2 + 1][col2 + 1] - self.sum_[row1][col2 + 1]
        sum_col1 = self.sum_[row2 + 1][col1] - self.sum_[row1][col1]
        return sum_col2 - sum_col1


class NumMatrixV0(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]

        beats 39.02%
        """
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                self.sums[i][j] = matrix[i - 1][j - 1] + self.sums[i][j - 1] + self.sums[i - 1][j] - self.sums[i - 1][
                    j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][
            col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
