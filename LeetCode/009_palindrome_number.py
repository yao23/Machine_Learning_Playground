class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        beats 41.60%
        """
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x / ranger
            right = x % 10
            if left != right:
                return False

            x = (x % ranger) / 10
            ranger /= 100

        return True