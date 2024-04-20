class Solution(object):
    """
    https://www.youtube.com/watch?v=-RDzMJ33nx8
    
    beats 5.02%
    """
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)] # take or skip current char in s
                else:
                    cache[(i, j)] = cache[(i + 1, j)] # skip current char in s
        return cache[(0, 0)]

    def numDistinctV0(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        O(n) space
        beats 70.80%
        """
        l1, l2 = len(s)+1, len(t)+1
        cur = [0] * l2
        cur[0] = 1
        for i in xrange(1, l1):
            pre = cur[:]
            for j in xrange(1, l2):
                cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
        return cur[-1]

    def numDistinct1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        O(m*n) space
        beats 4.40%
        """
        l1, l2 = len(s) + 1, len(t) + 1
        dp = [[1] * l2 for _ in xrange(l1)]
        for j in xrange(1, l2):
            dp[0][j] = 0
        for i in xrange(1, l1):
            for j in xrange(1, l2):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
        return dp[-1][-1]
