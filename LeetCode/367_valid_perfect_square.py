class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool

        beats 15.65%
        """
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num
