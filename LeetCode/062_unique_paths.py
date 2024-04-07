class Solution(object):
    def uniquePaths(self, m: int, n: int) -> int:
        """
        beats 75.15%
        """
        preRow = [0] * n
        for i in range(m - 1, -1, -1): # start from last row
            curRow = [0] * n
            curRow[n - 1] = 1
            for j in range(n - 2, -1, -1):
                curRow[j] = preRow[j] + curRow[j + 1] # sum down and right
            preRow = curRow
        return preRow[0]

    def uniquePaths(self, m: int, n: int) -> int:
        """
        https://www.youtube.com/watch?v=IlEsdxuD4lY
        
        beats 69.61%
        """
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]
        
    def uniquePathsV0(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        beats 29.74%
        """
        aux = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1] + aux[i-1][j]
        return aux[-1][-1]
