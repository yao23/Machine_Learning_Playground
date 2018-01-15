class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        Bottom up, constant space
        beats 33.40%
        """
        if n == 1:
            return 1
        a, b = 1, 2
        for i in xrange(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b

    def climbStairs0(self, n):
        """
        :type n: int
        :rtype: int

        Bottom up, O(n) space
        beats 33.40%
        """
        if n == 1:
            return 1
        res = [0 for i in xrange(n)]
        res[0], res[1] = 1, 2
        for i in xrange(2, n):
            res[i] = res[i - 1] + res[i - 2]
        return res[-1]

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int

        Top down + memorization (list)
        beats 20.08%
        """
        if n == 1:
            return 1
        dic = [-1 for _ in xrange(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]
