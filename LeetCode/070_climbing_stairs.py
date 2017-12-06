class Solution(object):
    # Bottom up, constant space
    # beats 33.40%
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for i in xrange(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b

    # Bottom up, O(n) space
    # beats 33.40%
    def climbStairs0(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]

    # Top down + memorization (list)
    # beats 20.08%
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dic = [-1 for i in xrange(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]