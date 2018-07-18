class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        beats 77.24%
        """
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1
