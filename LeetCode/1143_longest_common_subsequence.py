class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        beats 96.16%
        """
        row, col = len(text1), len(text2)
        if row == 0 or col == 0:
            return 0
        
        preRow = [0] * (col + 1)
        
        for i in range(row - 1, -1, -1):
            curRow = [0] * (col + 1)
            for j in range(col - 1, -1, -1):
                if text1[i] == text2[j]:
                    curRow[j] = preRow[j + 1] + 1
                else:
                    curRow[j] = max(preRow[j], curRow[j + 1])
            preRow = curRow

        return preRow[0]

  def longestCommonSubsequenceV0(self, text1: str, text2: str) -> int:
        """
        https://www.youtube.com/watch?v=Ua0GhsJSlWM
        
        beats 83.73%
        """
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
