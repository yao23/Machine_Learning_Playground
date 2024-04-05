def guess(num):
    """
    :param num:
    :return:

    The guess API is already defined for you.
    @param num, your guess
    @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
    """
    return num


class Solution(object):
    def guessNumber(self, n: int) -> int:
        """
        https://www.youtube.com/watch?v=xW4QsTtaCa4
        
        beats 17.85%
        """
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            tmp = guess(m)
            if tmp == 0:
                return m
            elif tmp == 1:
                l = m + 1
            else:
                r = m - 1
        return -1
        
    def guessNumberV0(self, n):
        """
        :type n: int
        :rtype: int

        beats 50.00%
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
