class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool

        beats 89.32%
        """
        return num != 0 and num & (num-1) == 0 and num & 1431655765 == num
