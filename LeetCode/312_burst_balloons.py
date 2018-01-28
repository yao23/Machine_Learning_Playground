class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Bottom-up
        refer to idea in following Top-down solution

        beats 71.05%
        """
        nums = [1] + nums + [1]  # build the complete array
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]

    def maxCoins1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Top-down

        find the last balloon and solve same sub-problem for left and right parts
        cache previous calculated results to speed up execution

        beats 33.33%
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:  # in memory or gap < 2
                return dp[i][j]
            coins = 0
            for k in range(i + 1, j):  # find the last balloon
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n - 1)
