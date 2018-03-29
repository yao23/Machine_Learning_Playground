import math


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int

        Catalan Number  (2n)!/((n+1)!*n!)
        beats 78.51%
        """
        return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))

    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int

        DP
        beats 32.81%
        """
        res = [0] * (n + 1)
        res[0] = 1
        for i in xrange(1, n + 1):  # i [1, n]
            for j in xrange(i):  # j: [0, i - 1]
                res[i] += (res[j] * res[i - 1 - j])
        return res[n]
