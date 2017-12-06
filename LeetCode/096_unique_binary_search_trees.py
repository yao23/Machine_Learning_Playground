import math

class Solution(object):
    # Catalan Number  (2n)!/((n+1)!*n!)
    # beats 78.51%
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))

    # DP
    # beats 32.81%
    def numTrees1(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n + 1)
        res[0] = 1
        for i in xrange(1, n + 1):
            for j in xrange(i):
                res[i] += res[j] * res[i - 1 - j]
        return res[n]