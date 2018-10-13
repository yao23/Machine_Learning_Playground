class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool

        beats 79.20%
        """
        return n > 0 and 1162261467 % n == 0
