class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

        beats 9.48%
        """
        return n > 0 and not (n & n-1)
