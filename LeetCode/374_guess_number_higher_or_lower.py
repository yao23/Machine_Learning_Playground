# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    # beats 50.00%
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l + 1 < r:
            m = l + (r - l) / 2
            res = guess(m)
            if res < 0:
                r = m
            elif res > 0:
                l = m
            else:
                return m

        if guess(l) == 0:
            return l
        if guess(r) == 0:
            return r
        return None