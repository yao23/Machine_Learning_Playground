class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        beats 38.89%
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        beats 37.38%
        """
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

    def spiralOrder2(self, matrix):
        """
        :param matrix:
        :return:

        beats 53.16%
        """
        res = []
        if not matrix or len(matrix) == 0:
            return res
        row = len(matrix)
        col = len(matrix[0])
        self.helper(res, matrix, row, col, 0)
        return res

    def helper(self, res, matrix, row, col, offset):
        """
        :param res:
        :param matrix:
        :param row:
        :param col:
        :param offset:
        :return:

        beats 53.16%
        """
        if row == 0 or col == 0:  # none left
            return
        if row == 1:  # one row left
            for i in range(offset, col + offset):
                res.append(matrix[offset][i])
            return
        if col == 1:  # one column left
            for i in range(offset, row + offset):
                res.append(matrix[i][offset])
            return

        # top row
        for i in range(offset, col - 1 + offset):
            res.append(matrix[offset][i])

        # right column
        for i in range(offset, row - 1 + offset):
            res.append(matrix[i][col - 1 + offset])

        # bottom row
        for i in range(col - 1 + offset, offset, -1):
            res.append(matrix[row - 1 + offset][i])

        # left column
        for i in range(row - 1 + offset, offset, -1):
            res.append(matrix[i][offset])

        self.helper(res, matrix, row - 2, col - 2, offset + 1)
