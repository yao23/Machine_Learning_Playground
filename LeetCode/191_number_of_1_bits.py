class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        beats 57.20%
        """
        return bin(n).count('1')

    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int

        beats 57.20%
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
