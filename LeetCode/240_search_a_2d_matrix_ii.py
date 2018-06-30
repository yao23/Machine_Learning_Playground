class Solution(object):
    def searchMatrix(self, mat, x):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        beats 44.95%
        """
        if mat:
            m, n, r, c = len(mat), len(mat[0]), 0,  len(mat[0]) - 1
            while r < m and c >= 0:
                if mat[r][c] == x:
                    return True
                if mat[r][c] < x:
                    r += 1
                else:
                    c -= 1
        return False
