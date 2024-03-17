class Solution(object):
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=OM1MTokvxs4&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=7
        
        beats 38.21%
        """
        dp = [0] * (len(triangle) + 1)
        for row in triangle[::-1]: # traverse in reversed order (bottom up)
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])
        return dp[0]
        
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        O(n*n/2) space, top-down
        beats 39.32%
        """
        if not triangle:
            return
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])

    def minimumTotal2(self, triangle):
        """
        :param triangle:
        :return:

        Modify the original triangle, top-down
        """
        if not triangle:
            return
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    def minimumTotal3(self, triangle):
        """
        :param triangle:
        :return:

        Modify the original triangle, bottom-up
        """
        if not triangle:
            return
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def minimumTotal0(self, triangle):
        """
        :param triangle:
        :return:

        bottom-up, O(n) space
        beats 56.20%
        """
        if not triangle:
            return
        res = triangle[-1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]
