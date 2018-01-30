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

    def maxCoins2(self, nums):
        """
        :param nums:
        :return:

        beats 17.54%
        """
        len_nums = len(nums)
        full_nums = [0] * (len_nums + 2)
        full_nums[0] = full_nums[-1] = 1
        for i, num in enumerate(nums):
            full_nums[i + 1] = num
        scores = [[-1 for _ in range(len_nums + 2)] for _ in range(len_nums + 2)]
        for row in range(len_nums):
            for col in range(len_nums):
                scores[row][col] = -1

        return self.get_scores(1, len_nums, scores, full_nums)

    def get_scores(self, start, end, scores, full_nums):
        if start > end:
            return 0
        if scores[start][end] != -1:
            return scores[start][end]
        for pos in range(start, end + 1):
            mid_coin_scores = full_nums[start - 1] * full_nums[pos] * full_nums[end + 1]
            left_coin_scores = self.get_scores(start, pos - 1, scores, full_nums)
            right_coin_scores = self.get_scores(pos + 1, end, scores, full_nums)
            cur_sum = left_coin_scores + mid_coin_scores + right_coin_scores
            if scores[start][end] < cur_sum:
                scores[start][end] = cur_sum

        return scores[start][end]
