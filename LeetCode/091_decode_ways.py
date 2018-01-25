class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int

        w tells the number of ways
        v tells the previous number of ways
        d is the current digit
        p is the previous digit

        beats 84.18%
        """
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w

    def numDecodings1(self, s):
        """
        :type s: str
        :rtype: int

        beats 29.80%
        """
        if s is None or len(s) == 0:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n + 1):
            first = int(s[i - 1: i])
            second = int(s[i - 2: i])
            if 1 <= first <= 9:
                dp[i] += dp[i - 1]
            if 10 <= second <= 26:
                dp[i] += dp[i - 2]
        return dp[n]

    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int

        beats 52.53%
        """
        if s == "":
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if i != 1 and "09" < s[i - 2:i] < "27":  # "01"ways = 0
                dp[i] += dp[i - 2]
        return dp[len(s)]
