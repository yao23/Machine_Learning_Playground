class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=d3UOz7zdE4I
    
        beats 59.61%
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N-1] = 1

        # Time: O(N*M), Space: O(N)
        for r in reversed(range(M)): # from last row (reversed iteration)
            for c in reversed(range(N)): # from last column (reversed iteration)
                if obstacleGrid[r][c]: # obstacle
                    dp[c] = 0
                elif c + 1 < N: # valid column
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]

    def uniquePathsWithObstaclesV2(self, obstacleGrid: List[List[int]]) -> int:
        """
        recursive with memoization (dp map)

        
        # Time: O(N*M), Space: O(N*M)
        # beats 36.32%
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(M - 1, N - 1): 1}

        def dfs(r, c):
            if r == M or c == N or obstacleGrid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]
        return dfs(0, 0)
    
    def uniquePathsWithObstaclesV1(self, obstacleGrid: List[List[int]]) -> int:
        """
        beats 63.55%
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        preRow = [0] * n # the row under last row with all zeros
        preRow[n - 1] = 1
        for i in range(m - 1, -1, -1): # start from last row
            curRow = [0] * n
            if obstacleGrid[i][n - 1] == 0 and preRow[n - 1]: # can go down
                curRow[n - 1] = 1
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:    
                    curRow[j] = preRow[j] + curRow[j + 1] # sum down and right
            preRow = curRow
        return preRow[0]
        
    def uniquePathsWithObstaclesV0(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        beats 61.37%
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
