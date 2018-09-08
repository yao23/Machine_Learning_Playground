class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool

        beats 51.25%
        """
        return bool(n % 4)
