class Solution(object):
    """
    https://www.youtube.com/watch?v=XYi2-LPrwm4

    Memozization
    
    beats 86.63%
    """
    def minDistanceV0(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(word1): 
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]
            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(
                    dfs(i, j + 1),    # insert
                    dfs(i + 1, j),    # delete
                    dfs(i + 1, j + 1) # replace
                )
            return dp[(i, j)]

        return dfs(0, 0)
        
    def minDistanceV2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        DP (top down)

        O(m*n) space
        beats 54.30%
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return dp[-1][-1]

    """
    DP (bottom up) - converted from V0 (memozization)
    
    beats 66.45%
    """
    def minDistanceV3(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j  # left to right in bottom row
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i  # up to down in right column

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]


    def minDistance1(self, word1, word2):
        """
        :param word1:
        :param word2:
        :return:

        O(n) space with rolling array
        beats 87.02%
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [0 for _ in range(l2)]
        for j in range(l2):
            pre[j] = j
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]
