class Solution(object):
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    # beats 61.37%
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, n):
            if not obstacleGrid[0][i]:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]
            else:
                obstacleGrid[0][i] = 0

        for i in range(1, m):
            if not obstacleGrid[i][0]:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]
            else:
                obstacleGrid[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]