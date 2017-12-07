class Solution(object):
    # beats 15.65%
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r) / 2
        return r*r == num
