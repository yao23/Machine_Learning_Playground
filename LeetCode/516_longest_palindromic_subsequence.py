class Solution:
    """
    https://www.youtube.com/watch?v=bUr8cNWI09Q
    
    DP

    beats 35.27%
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        res = 0

        for i in range(len(s)): # left pointer i
            for j in range(len(s) - 1, i - 1, -1): # right pointer j moving range [i, len(s) - 1] 
                if s[i] == s[j]:
                    length = 1 if i == j else 2
                    dp[i][j] = length + dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])

                res = max(res, dp[i][j])

        return res
  
    """
    Memozization
    
    Time / Memory Limit Exceeded
    """
    def longestPalindromeSubseqV0(self, s: str) -> int:
        mem = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            if s[i] == s[j]: # same and expance to left and right
                length = 1 if i == j else 2
                mem[(i, j)] = length + dfs(i - 1, j + 1)
            else: # not same and either move to left or right
                mem[(i, j)] = max(
                  dfs(i - 1, j), # move to left
                  dfs(i, j + 1)) # move to right

            return mem[(i, j)]

        res = 0
        for i in range(len(s)):
            res = max(
                res, 
                dfs(i, i),    # odd number palindrome subsequence
                dfs(i, i + 1) # even number palindrome subsequence
            )
        return res

    """
    https://www.youtube.com/watch?v=bUr8cNWI09Q

    longestCommonSubsequence for string and reversed string
    
    beats 32.94%
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        def longestCommonSubsequence(s1, s2):
            N, M = len(s1), len(s2)
            dp = [[0] * (M + 1) for _ in range(N + 1)]

            for i in range(N):
                for j in range(M):
                    if s1[i] == s2[j]:
                        dp[i + 1][j + 1] = 1 + dp[i][j]
                    else:
                        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

            return dp[N][M]

        return longestCommonSubsequence(s, s[::-1]) # s and reversed s
