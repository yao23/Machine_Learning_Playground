class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int

        beats 98.73%
        """
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < row - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < col - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        return max(dfs(x, y) for x in range(row) for y in range(col))
