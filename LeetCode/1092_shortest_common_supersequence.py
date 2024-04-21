class Solution:
    """
    https://leetcode.com/problems/shortest-common-supersequence/solutions/2219006/python3-concise-recursion-memoization
    
    beats 5.08%
    """
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @lru_cache(maxsize= 8000)
        def helper(first: str, second: str):
            
            if not first and not second:
                return ""
            
            if not first:
                return second
            
            if not second:
                return first
            
            if first[0] == second[0]:
                return first[0] + helper(first[1:], second[1:])
            
            right = second[0] + helper(first, second[1:])
            left = first[0] + helper(first[1:], second)
            
            if len(right) > len(left):
                return left
            return right
            
        return helper(str1, str2)

  """
  https://leetcode.com/problems/shortest-common-supersequence/solutions/3501177/day-403-easy-lcs-0ms-100-python-java-c-explained-approach
  
  beats 95.07%
  """
  def shortestCommonSupersequenceV1(self, str1: str, str2: str) -> str:
        s1, s2 = str1, str2
        # find the LCS of s1 and s2
        lcs = self.getLCS(s1, s2)
        i, j = 0, 0
        result = ""
        # merge s1 and s2 with the LCS
        for c in lcs:
            # add characters from s1 until the LCS character is found
            while s1[i] != c:
                result += s1[i]
                i += 1
            # add characters from s2 until the LCS character is found
            while s2[j] != c:
                result += s2[j]
                j += 1
            # add the LCS character
            result += c
            i += 1
            j += 1
        # add any remaining characters from s1 and s2
        result += s1[i:] + s2[j:]
        # return the merged string
        return result

    # helper method to find the LCS of two strings
    def getLCS(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # fill the dp array using dynamic programming
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # backtrack from the bottom right corner of the dp array to find the LCS
        lcs = ""
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs = s1[i-1] + lcs
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return lcs

    """
    wrong answer

    Input
    str1 = "abac"
    str2 = "cab"
    
    Output: "caabac"
    Expected: "cabac"
    """
    def shortestCommonSupersequenceV0(self, str1: str, str2: str) -> str:
        res = ""
        resLen = float("inf")
        dp = {}

        def dfs(i, j, tmp):
            nonlocal res, resLen, dp

            if i == len(str1):
                if len(tmp) + len(str2) - j < resLen:
                    resLen = len(tmp) + len(str2) - j
                    res = str(tmp + str2[j:])
                    return len(str2) - j
                return float("inf")

            if j == len(str2):
                if len(tmp) + len(str1) - i < resLen:
                    resLen = len(tmp) + len(str1) - i
                    res = str(tmp + str1[i:])
                    return len(str1) - i
                return float("inf")
            
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = min(
                    dfs(i, j + 1, tmp + str2[j]),
                    dfs(i + 1, j, tmp + str1[i])
                ) + 1
            if str1[i] == str2[j]:
                dp[(i, j)] = min(
                    dp[(i, j)],
                    dfs(i + 1, j + 1, tmp + str1[i]) + 1
                )

            return dp[(i, j)]

        dfs(0, 0, "")
        return res
