class NumMatrix(object):
    """
    Your NumMatrix object will be instantiated and called as such:
    obj = NumMatrix(matrix)
    obj.update(row,col,val)
    param_2 = obj.sumRegion(row1,col1,row2,col2)

    https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75872/Python-94.5-Simple-sum-array-on-one-dimension-O(n)-for-both-update-and-sum

    beats 83.86%
    """

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        for row in matrix:
            for col in range(1, len(row)):
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

        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        region_sum = 0
        for x in range(row1, row2 + 1):
            region_sum += self.matrix[x][col2]
            if col1 != 0:
                region_sum -= self.matrix[x][col1 - 1]
        return region_sum
