class Solution(object):
    # beats 45.07%
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, inv = 1, 1, 1
        while n > 1: start, size, inv, n = start + inv * size + 2 * (n // 2 - 1) * inv * size,\
                                          size * 2, inv * -1,\
                                          n // 2
        return start