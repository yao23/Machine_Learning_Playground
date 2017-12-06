class Solution(object):
    # beats 47.64%
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i and j:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
        return len(matrix) and max(map(max, matrix)) ** 2

    # beats 54.25%
    def maximalSquare1(self, A):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        area = 0
        if A:
            p = [0] * len(A[0])
            for row in A:
                s = map(int, row)
                for j, c in enumerate(s[1:], 1):
                    s[j] *= min(p[j - 1], p[j], s[j - 1]) + 1
                area = max(area, max(s) ** 2)
                p = s
        return area