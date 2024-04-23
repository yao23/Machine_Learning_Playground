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
        for i in range(2, n):
            tmp = b
            b = a + b
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
        res = [0 for _ in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
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
        dic = [-1 for _ in range(n)]
        dic[0], dic[1] = 1, 2
        return self.helper(n - 1, dic)

    def helper(self, n, dic):
        if dic[n] < 0:
            dic[n] = self.helper(n - 1, dic) + self.helper(n - 2, dic)
        return dic[n]

    """
    https://www.youtube.com/watch?v=Y0lT9Fck7qI
    
    beats 59.08%
    """
    def climbStairsV2(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2
